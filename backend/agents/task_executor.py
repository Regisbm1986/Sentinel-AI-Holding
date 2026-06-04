from backend.agents.workflow_state_manager import WorkflowStateManager


class TaskExecutor:

    WORKFLOW_STATES = (
        "approved",
        "planned",
        "reviewing",
        "completed"
    )

    def __init__(self):

        self.workflow = WorkflowStateManager()

    def execute(self, task_id):

        for state in self.WORKFLOW_STATES:
            final_status = self.workflow.set_state(task_id, state)

        return final_status
