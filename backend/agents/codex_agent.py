import json
import os

from backend.core.config import AGENT_TASKS_DIR


class CodexAgent:

    TASK_PATH = AGENT_TASKS_DIR

    def get_next_task(self):

        path = os.path.join(
            self.TASK_PATH,
            "approved.json"
        )

        with open(path, "r") as f:

            tasks = json.load(f)

        if not tasks:

            return {
                "status": "no_tasks"
            }

        return tasks[0]

    def generate_task_context(self):

        task = self.get_next_task()

        if task == {"status": "no_tasks"}:

            return {
                "status": "no_tasks"
            }

        return {
            "status": "task_ready",
            "task": task,
            "context": {
                "project": "Sentinel OS",
                "agent": "CodexAgent"
            }
        }

    def generate_execution_plan(self):

        task_context = self.generate_task_context()

        if task_context["status"] == "no_tasks":

            return {
                "status": "no_tasks"
            }

        return {
            "status": "plan_ready",
            "task": task_context["task"],
            "steps": [
                "analyze",
                "implement",
                "review"
            ]
        }
