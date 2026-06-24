from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI(title="For-me - Virtual MVP Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# in-memory store of latest device states
devices = {}

class SimPayload(BaseModel):
    device_id: str
    type: str | None = None
    value: float | None = None
    ts: float | None = None

@app.post("/simulate")
async def simulate(payload: SimPayload):
    ts = payload.ts or time.time()
    devices[payload.device_id] = {
        "device_id": payload.device_id,
        "type": payload.type or "unknown",
        "value": payload.value,
        "ts": ts,
    }
    return {"status": "ok"}

@app.get("/devices")
async def get_devices():
    return {"devices": list(devices.values())}

@app.get("/")
async def root():
    return {"message": "For-me backend running"}
