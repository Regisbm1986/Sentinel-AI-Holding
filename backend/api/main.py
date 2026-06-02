from fastapi import FastAPI

from backend.api.routes.enum4linux import router as enum4linux_router
from backend.api.routes.nikto import router as nikto_router
from backend.api.routes.spiderfoot import router as spiderfoot_router
from backend.api.routes.system import router as system_router


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


for api_router in (
    nikto_router,
    spiderfoot_router,
    enum4linux_router,
    system_router,
):
    app.include_router(api_router, prefix="/api")
