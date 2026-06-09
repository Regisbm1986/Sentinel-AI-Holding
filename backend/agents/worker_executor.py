from backend.agents.task_result_manager import TaskResultManager


class WorkerExecutor:
    def __init__(self):
        self.results = TaskResultManager()

    def execute(self, worker_id, task_id):
        result = {
            "worker_id": worker_id,
            "task_id": task_id,
            "status": "completed"
        }

        self.results.save_result(
            task_id,
            result
        )

        return result
