from fastapi import FastAPI, HTTPException
from app.config import settings
from app.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator(settings)

@app.post("/chat")
async def chat(payload: dict):
    message = payload.get("message")
    mode = payload.get("mode", "answer")
    if not message:
        raise HTTPException(400, "message is required")
    if mode not in ("answer", "prompt"):
        raise HTTPException(400, "mode must be 'answer' or 'prompt'")
    response = await orch.route(message, mode)
    return {"response": response}