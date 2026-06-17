import importlib
from pathlib import Path

from fastapi import FastAPI

from backend.api.control import (
    get_autonomous_status,
    get_goals,
    get_telemetry,
    get_workers,
    run_autonomous_cycle,
)
from backend.agents.autonomous_developer import AutonomousDeveloper
from backend.agents.orchestrator import Orchestrator
from backend.agents.task_queue import TaskQueue
from backend.agents.worker_selector import WorkerSelector
from backend.telemetry.execution_telemetry import ExecutionTelemetry
from backend.core.config import PROJECT_ROOT


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


@app.post("/autonomous/run")
def autonomous_run():
    return run_autonomous_cycle(
        project_root=PROJECT_ROOT,
        developer_cls=AutonomousDeveloper,
        orchestrator_cls=Orchestrator,
    )


@app.get("/autonomous/status")
def autonomous_status():
    return get_autonomous_status(task_queue_cls=TaskQueue)


@app.get("/telemetry")
def telemetry():
    return get_telemetry(telemetry_cls=ExecutionTelemetry)


@app.get("/workers")
def workers():
    return get_workers(worker_selector_cls=WorkerSelector)


@app.get("/goals")
def goals():
    return get_goals(project_root=PROJECT_ROOT, developer_cls=AutonomousDeveloper)



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
