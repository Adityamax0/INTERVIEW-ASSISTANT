"""
main.py

FastAPI backend for the Aditya AI Interview Assistant.

Endpoints:
  POST /session                    -> create a new session, returns session_id
  POST /session/{id}/chat          -> send an HR message, get Aditya's (AI) reply
  POST /session/{id}/upload-jd     -> upload a PDF/DOCX job description
  GET  /session/{id}/exists        -> check a session is still alive

Run locally:
  uvicorn main:app --reload
"""

import os
import tempfile
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import sessions
from jd_parser import parse_job_description_file, UnsupportedFileType

app = FastAPI(title="Aditya AI Interview Assistant")

# Restrict this to your actual frontend domain(s) once deployed --
# "*" is fine for local dev only.
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


class SessionResponse(BaseModel):
    session_id: str


class JDUploadResponse(BaseModel):
    role_title: str
    message: str


@app.post("/session", response_model=SessionResponse)
def create_session():
    session_id = sessions.create_session()
    return {"session_id": session_id}


@app.get("/session/{session_id}/exists")
def session_exists(session_id: str):
    return {"exists": sessions.session_exists(session_id)}


@app.post("/session/{session_id}/chat")
def chat(session_id: str, req: ChatRequest):
    brain = sessions.get_brain(session_id)
    if brain is None:
        raise HTTPException(status_code=404, detail="Session not found.")

    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    return StreamingResponse(
        brain.ask_stream(req.message),
        media_type="text/plain",
    )


@app.post("/session/{session_id}/upload-jd", response_model=JDUploadResponse)
async def upload_jd(session_id: str, file: UploadFile = File(...)):
    brain = sessions.get_brain(session_id)
    if brain is None:
        raise HTTPException(status_code=404, detail="Session not found.")

    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in (".pdf", ".docx"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are accepted for job descriptions.",
        )

    # Write to a temp file since jd_parser works off a file path.
    with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        jd_json = parse_job_description_file(tmp_path)
    except UnsupportedFileType as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    finally:
        os.remove(tmp_path)

    brain.set_job_description(jd_json)

    role_title = jd_json.get("role_title") or "the uploaded role"
    return {
        "role_title": role_title,
        "message": f"Job description loaded: {role_title}. Answers will now be judged against this role.",
    }
