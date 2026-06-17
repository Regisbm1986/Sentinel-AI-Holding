from backend.agents.autonomous_developer import AutonomousDeveloper
from backend.agents.orchestrator import Orchestrator
from backend.agents.task_queue import TaskQueue
from backend.agents.worker_selector import WorkerSelector
from backend.telemetry.execution_telemetry import ExecutionTelemetry
from backend.core.config import PROJECT_ROOT


def run_autonomous_cycle(
    project_root=PROJECT_ROOT,
    developer_cls=AutonomousDeveloper,
    orchestrator_cls=Orchestrator,
):
    developer = developer_cls(project_root=project_root)
    developer.execute_discovered_goals()

    orchestrator = orchestrator_cls()
    result = orchestrator.process_queue()

    return {
        "status": result.get("status"),
        "result": result,
    }


def get_autonomous_status(task_queue_cls=TaskQueue):
    queue = task_queue_cls()
    next_task = queue.peek_next_task()

    return {
        "queue_status": "empty" if next_task is None else "pending",
        "next_task": next_task,
    }


def get_telemetry(telemetry_cls=ExecutionTelemetry):
    telemetry = telemetry_cls()
    return telemetry.get_logs()


def get_workers(worker_selector_cls=WorkerSelector):
    selector = worker_selector_cls()
    return {
        "available_workers": selector.get_available_workers(),
    }


def get_goals(project_root=PROJECT_ROOT, developer_cls=AutonomousDeveloper):
    developer = developer_cls(project_root=project_root)
    return {
        "goals": developer.discover_goals(),
    }