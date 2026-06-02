import os

from backend.core.config import API_ROUTES_DIR, API_SCHEMAS_DIR
from backend.agents.agent_controller import AgentController


class ReviewAgent:

    def review_routes(self):

        findings = []

        routes_path = API_ROUTES_DIR

        schemas_path = API_SCHEMAS_DIR

        for file in os.listdir(routes_path):

            if not file.endswith(".py"):
                continue

            if file == "__init__.py":
                continue

            schema_name = file

            schema_file = os.path.join(
                schemas_path,
                schema_name
            )

            if not os.path.exists(schema_file):

                findings.append({
                    "issue":
                    f"Schema ausente para {file}",
                    "priority":
                    "high"
                })

        return findings

    def create_review_tasks(self):

        findings = self.review_routes()

        controller = AgentController()

        created = []

        for finding in findings:

            controller.add_task(
                finding["issue"],
                finding["priority"]
            )

            created.append(
                finding["issue"]
            )

        return created
