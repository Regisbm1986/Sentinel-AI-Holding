from fastapi import FastAPI
from backend.api.routes.nikto import router as nikto_router
from pydantic import BaseModel
from fastapi import APIRouter
from backend.api.routes.spiderfoot import router as spiderfoot_router
from backend.api.routes.enum4linux import router as enum4linux_router

router = APIRouter()


class NiktoRequest(BaseModel):
    target: str


@router.post("/nikto")
def run_nikto_scan(payload: NiktoRequest):

    return {
        "module": "nikto",
        "target": payload.target,
        "status": "queued"
    }

app = FastAPI(
    title="Sentinel OS API",
    version="2.0.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "framework": "Sentinel OS",
        "version": "2.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(
    nikto_router,
    prefix="/api"
)

app.include_router(
    spiderfoot_router,
    prefix="/api"
)

app.include_router(
    enum4linux_router,
    prefix="/api"
)
