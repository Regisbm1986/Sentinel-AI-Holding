import importlib
from pathlib import Path

from fastapi import FastAPI


ROUTES_DIR = Path(__file__).resolve().parent / "routes"
MODULE_PREFIX = "backend.api.routes"


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




def register_routes(app, routes_dir=ROUTES_DIR, module_prefix=MODULE_PREFIX):
    for route_file in sorted(routes_dir.glob("*.py")):
        if route_file.name.startswith("__") or route_file.name == "main.py":
            continue

        module_name = f"{module_prefix}.{route_file.stem}"
        module = importlib.import_module(module_name)
        router = getattr(module, "router", None)

        if router is not None:
            app.include_router(router, prefix="/api")

    return app


register_routes(app)
