from backend.agents.worker_dispatcher import WorkerDispatcher
from backend.agents.worker_executor import WorkerExecutor


class Orchestrator:
    def __init__(self):
        self.dispatcher = WorkerDispatcher()
        self.executor = WorkerExecutor()

    def run_task(self, task_id):
        dispatch = self.dispatcher.dispatch(task_id)

        if dispatch["status"] != "dispatched":
            return dispatch

        return self.executor.execute(
            dispatch["worker_id"],
            task_id
        )
