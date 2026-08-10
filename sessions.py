"""
sessions.py

Holds one InterviewBrain per session_id so concurrent HR visitors never
share (or overwrite) each other's conversation.

In-memory dict for now. When the database is added, replace the dict
with reads/writes to a `sessions` + `messages` table -- the public
functions below (create_session, get_brain, session_exists) are the
seam to swap out, so main.py won't need to change.
"""

import uuid

from brain import InterviewBrain

_sessions: dict[str, InterviewBrain] = {}


def create_session() -> str:
    session_id = str(uuid.uuid4())
    _sessions[session_id] = InterviewBrain()
    return session_id


def session_exists(session_id: str) -> bool:
    return session_id in _sessions


def get_brain(session_id: str) -> InterviewBrain | None:
    return _sessions.get(session_id)


def delete_session(session_id: str) -> None:
    _sessions.pop(session_id, None)
