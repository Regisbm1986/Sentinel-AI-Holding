from backend.agents.backend_agent import BackendAgent
from backend.agents.codex_agent import CodexAgent


class OrchestratorAgent:

    def execute_task(self):

        codex_agent = CodexAgent()

        cycle_result = codex_agent.execute_cycle()

        if cycle_result["status"] == "no_tasks":

            return {
                "status": "no_tasks"
            }

        task = cycle_result["task"]
        plan = cycle_result["plan"]
        review = cycle_result["review"]

        backend_agent = BackendAgent()

        implementation_plan = backend_agent.generate_implementation_plan(
            task
        )

        return {
            "status": "orchestration_completed",
            "task": task,
            "plan": plan,
            "review": review,
            "implementation": implementation_plan
        }
