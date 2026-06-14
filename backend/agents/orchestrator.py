from backend.agents.worker_dispatcher import WorkerDispatcher
from backend.agents.worker_executor import WorkerExecutor
from backend.agents.agent_memory import AgentMemory
from backend.agents.task_history import TaskHistory
from backend.agents.workflow_state_manager import WorkflowStateManager
from backend.agents.task_queue import TaskQueue

class Orchestrator:
    def __init__(self):
        self.dispatcher = WorkerDispatcher()
        self.executor = WorkerExecutor()
        self.memory = AgentMemory()
        self.history = TaskHistory()
        self.workflow = WorkflowStateManager()
        self.queue = TaskQueue()

    def process_queue(self):

        task = self.queue.get_next_task()

        if not task:

            return {
                "status": "empty_queue"
            }

        return self.run_task(task)

    def run_task(self, task):

        task_key = str(task)

        self.workflow.set_state(
            task_key,
            "planned"
        )

        dispatch = self.dispatcher.dispatch(task)

        if dispatch["status"] != "dispatched":

            self.workflow.set_state(
                task_key,
                "failed"
            )

            return dispatch

        self.workflow.set_state(
            task_key,
            "dispatched"
        )

        self.workflow.set_state(
            task_key,
            "running"
        )

        result = self.executor.execute(
            dispatch["worker_id"],
            task
        )

        self.workflow.set_state(
            task_key,
            "completed"
        )

        self.history.log_event(
            task_key,
            {
                "status": "completed",
                "worker_id": dispatch["worker_id"]
            }
        )

        self.memory.remember(
            {
                "task_id": task_key,
                "result": result
            }
        )

        return result
