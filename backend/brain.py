"""
brain.py

The AI brain for the Aditya AI Interview Assistant.

Each InterviewBrain instance is now scoped to ONE session (one HR
conversation). sessions.py is responsible for creating/holding one
instance per session_id — this file has no notion of "the" brain
anymore, only "a" brain.

New in this version:
- Optional job_description (structured JSON, produced by jd_parser.py)
  can be attached to a session. When present, it's folded into the
  system message so the LLM judges Aditya's fit for that specific role
  honestly — same honesty rules as before, now with a JD to compare
  against.
- Token-budget based trimming instead of a flat message-count cap, so a
  normal-length interview is very unlikely to ever get trimmed.
"""

import os
import json
from dotenv import load_dotenv
from groq import Groq

from system_prompt import SYSTEM_PROMPT
from candidate_profile import CANDIDATE_PROFILE

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Rough token budget for the whole request (system + history + next
# reply). llama-3.3-70b-versatile has a large context window, so this is
# a conservative ceiling, not a hard model limit. Trimming only kicks in
# once we're close to it -- a normal interview won't get near this.
MAX_CONTEXT_TOKENS = 6000

# ~4 chars/token is a standard rough estimate for English text and is
# good enough for a trim heuristic (we don't need exact tokenization
# here, just to avoid ever silently overflowing the model).
CHARS_PER_TOKEN_ESTIMATE = 4


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN_ESTIMATE)


class InterviewBrain:
    def __init__(self, job_description: dict | None = None):
        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found. Make sure it's set in your .env file."
            )

        self.client = Groq(api_key=GROQ_API_KEY)

        # job_description is optional and can be attached later via
        # set_job_description() once HR uploads a JD mid-conversation.
        self.job_description = job_description

        # Conversation memory: only user/assistant turns live here.
        # The system message is rebuilt each call so it always reflects
        # the current job_description.
        self.history = []

    def set_job_description(self, job_description: dict) -> None:
        """Attach (or replace) the structured JD for this session."""
        self.job_description = job_description

    def _build_system_message(self) -> dict:
        parts = [
            SYSTEM_PROMPT,
            "\n\n## Candidate Profile (JSON)\n",
            json.dumps(CANDIDATE_PROFILE, indent=2),
        ]

        if self.job_description:
            parts.append(
                "\n\n## Job Description for this interview (JSON)\n"
                "HR has provided the following role details. Judge "
                "Aditya's fit against this honestly -- where the "
                "candidate profile is missing something this JD "
                "requires, say so plainly. Do not soften or omit gaps.\n"
            )
            parts.append(json.dumps(self.job_description, indent=2))

        return {"role": "system", "content": "".join(parts)}

    def _trimmed_history(self, system_message: dict) -> list:
        """
        Drop oldest user/assistant turns only if the estimated total
        token count (system + history) is approaching the budget.
        Keeps the whole session in memory otherwise.
        """
        budget = MAX_CONTEXT_TOKENS - _estimate_tokens(system_message["content"])
        kept = []
        running = 0

        # Walk from newest to oldest, keep what fits, then re-reverse.
        for msg in reversed(self.history):
            msg_tokens = _estimate_tokens(msg["content"])
            if running + msg_tokens > budget:
                break
            kept.append(msg)
            running += msg_tokens

        kept.reverse()
        return kept

    def _build_messages(self) -> list:
        system_message = self._build_system_message()
        return [system_message] + self._trimmed_history(system_message)

    def ask(self, hr_input: str) -> str:
        """
        Accepts one HR question, calls Groq, stores both sides of the
        exchange in memory, and returns the assistant's reply text.
        """
        self.history.append({"role": "user", "content": hr_input})

        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=self._build_messages(),
                temperature=0.4,
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = (
                "Sorry, I ran into an issue reaching the AI service "
                f"({e.__class__.__name__}). Please try again."
            )
            # Roll back the user message so a failed call doesn't pollute
            # memory with an unanswered question sitting in history.
            self.history.pop()
            return reply

        self.history.append({"role": "assistant", "content": reply})
        return reply


def main():
    """Kept for local CLI testing -- not used by the API."""
    print("Aditya AI Interview Assistant (CLI mode)")
    print("Type 'exit' or 'quit' to end the interview.\n")

    brain = InterviewBrain()

    while True:
        hr_input = input("HR: ").strip()
        if hr_input.lower() in ("exit", "quit"):
            print("Interview ended.")
            break
        if not hr_input:
            continue

        answer = brain.ask(hr_input)
        print(f"Aditya (AI): {answer}\n")


if __name__ == "__main__":
    main()
