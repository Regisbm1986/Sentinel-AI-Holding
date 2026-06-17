from backend.api.control import get_autonomous_status, get_goals, get_telemetry, get_workers
from backend.agents.task_queue import TaskQueue
from backend.agents.worker_selector import WorkerSelector
from backend.core.config import PROJECT_ROOT
from backend.database.capability_registry import CapabilityRegistry
from backend.telemetry.execution_telemetry import ExecutionTelemetry


def load_goals(project_root=PROJECT_ROOT):
    return get_goals(project_root=project_root).get("goals", [])


def load_queue_status(task_queue_cls=TaskQueue):
    return get_autonomous_status(task_queue_cls=task_queue_cls)


def load_workers(worker_selector_cls=WorkerSelector):
    return get_workers(worker_selector_cls=worker_selector_cls).get("available_workers", [])


def load_telemetry(telemetry_factory=ExecutionTelemetry, limit=25):
    telemetry = telemetry_factory()
    return telemetry.get_logs(limit=limit)


def load_capability_registry(registry_factory=CapabilityRegistry, status=None):
    registry = registry_factory()
    return registry.list_capabilities(status=status)


def derive_autonomous_execution_status(queue_status, telemetry_entries):
    last_entry = telemetry_entries[-1] if telemetry_entries else None
    queue_state = queue_status.get("queue_status", "unknown")

    if last_entry and last_entry.get("status") == "running":
        state = "running"
    elif queue_state == "pending":
        state = "queued"
    elif last_entry and last_entry.get("status") == "failed":
        state = "error"
    elif queue_state == "empty":
        state = "idle"
    else:
        state = "unknown"

    return {
        "state": state,
        "queue_status": queue_state,
        "next_task": queue_status.get("next_task"),
        "last_status": last_entry.get("status") if last_entry else None,
        "last_goal": last_entry.get("goal") if last_entry else None,
        "last_worker": last_entry.get("worker") if last_entry else None,
        "telemetry_entries": len(telemetry_entries),
    }


def build_dashboard_snapshot(
    project_root=PROJECT_ROOT,
    task_queue_cls=TaskQueue,
    worker_selector_cls=WorkerSelector,
    telemetry_factory=ExecutionTelemetry,
    registry_factory=CapabilityRegistry,
    telemetry_limit=25,
):
    goals = load_goals(project_root=project_root)
    queue_status = load_queue_status(task_queue_cls=task_queue_cls)
    workers = load_workers(worker_selector_cls=worker_selector_cls)
    telemetry = load_telemetry(telemetry_factory=telemetry_factory, limit=telemetry_limit)
    capabilities = load_capability_registry(registry_factory=registry_factory)
    execution_status = derive_autonomous_execution_status(queue_status, telemetry)

    return {
        "goals": goals,
        "queue_status": queue_status,
        "workers": workers,
        "telemetry": telemetry,
        "capabilities": capabilities,
        "execution_status": execution_status,
    }


def render_dashboard(snapshot=None):
    import streamlit as st

    if snapshot is None:
        snapshot = build_dashboard_snapshot(project_root=PROJECT_ROOT)

    st.set_page_config(
        page_title="Sentinel Operations Dashboard",
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Sentinel Operations Dashboard")
    st.caption("Read-only operational view backed by live Sentinel project data.")

    goals = snapshot["goals"]
    queue_status = snapshot["queue_status"]
    workers = snapshot["workers"]
    telemetry = snapshot["telemetry"]
    capabilities = snapshot["capabilities"]
    execution_status = snapshot["execution_status"]

    metrics = st.columns(6)
    metrics[0].metric("Goals", len(goals))
    metrics[1].metric("Queue", queue_status.get("queue_status", "unknown"))
    metrics[2].metric("Workers", len(workers))
    metrics[3].metric("Telemetry", len(telemetry))
    metrics[4].metric("Capabilities", len(capabilities))
    metrics[5].metric("Autonomous Status", execution_status["state"])

    tabs = st.tabs([
        "Goals",
        "Queue Status",
        "Workers",
        "Telemetry",
        "Capability Registry",
        "Autonomous Execution Status",
    ])

    with tabs[0]:
        st.subheader("Goals")
        if goals:
            st.table([{ "goal": goal } for goal in goals])
        else:
            st.info("No goals discovered in the current project.")

    with tabs[1]:
        st.subheader("Queue Status")
        st.metric("Queue State", queue_status.get("queue_status", "unknown"))
        next_task = queue_status.get("next_task")
        if next_task is not None:
            st.json(next_task)
        else:
            st.info("No queued task is waiting for execution.")

    with tabs[2]:
        st.subheader("Workers")
        if workers:
            st.table([{ "worker": worker } for worker in workers])
        else:
            st.info("No available workers were reported by the worker selector.")

    with tabs[3]:
        st.subheader("Telemetry")
        if telemetry:
            st.table(telemetry)
        else:
            st.info("No telemetry entries have been recorded yet.")

    with tabs[4]:
        st.subheader("Capability Registry")
        if capabilities:
            st.table(capabilities)
        else:
            st.info("The capability registry is empty.")

    with tabs[5]:
        st.subheader("Autonomous Execution Status")
        st.metric("State", execution_status["state"])
        st.write({
            "queue_status": execution_status["queue_status"],
            "telemetry_entries": execution_status["telemetry_entries"],
            "last_status": execution_status["last_status"],
            "last_goal": execution_status["last_goal"],
            "last_worker": execution_status["last_worker"],
        })


def main():
    render_dashboard()


if __name__ == "__main__":
    main()