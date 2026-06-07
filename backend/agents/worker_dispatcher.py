from backend.agents.remote_worker_manager import RemoteWorkerManager


class WorkerDispatcher:

    def __init__(self):

        self.worker_manager = RemoteWorkerManager()

    def get_available_worker(self):

        workers = self.worker_manager.get_workers()

        if not workers:

            return None

        return workers[0]

    def dispatch(self, task_id):

        worker_id = self.get_available_worker()

        if worker_id is None:

            return {
                "status": "no_workers"
            }

        return {
            "status": "dispatched",
            "worker_id": worker_id,
            "task_id": task_id
        }
