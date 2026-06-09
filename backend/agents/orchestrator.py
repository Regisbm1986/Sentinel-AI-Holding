from backend.agents.worker_dispatcher import WorkerDispatcher
from backend.agents.worker_executor import WorkerExecutor
from backend.agents.agent_memory import AgentMemory
from backend.agents.task_history import TaskHistory
from backend.agents.workflow_state_manager import WorkflowStateManager


class Orchestrator:
    def __init__(self):
        self.dispatcher = WorkerDispatcher()
        self.executor = WorkerExecutor()
        self.memory = AgentMemory()
        self.history = TaskHistory()
        self.workflow = WorkflowStateManager()

    def run_task(self, task_id):

        self.workflow.set_state(
            task_id,
            "planned"
        )

        dispatch = self.dispatcher.dispatch(task_id)

        if dispatch["status"] != "dispatched":

            self.workflow.set_state(
                task_id,
                "failed"
            )

            return dispatch

        self.workflow.set_state(
            task_id,
            "dispatched"
        )

        self.workflow.set_state(
            task_id,
            "running"
        )

        result = self.executor.execute(
            dispatch["worker_id"],
            task_id
        )

        self.workflow.set_state(
            task_id,
            "completed"
        )

        self.history.log_event(
            task_id,
            {
                "status": "completed",
                "worker_id": dispatch["worker_id"]
            }
        )

        self.memory.remember(
            {
                "task_id": task_id,
                "result": result
            }
        )

        return result
