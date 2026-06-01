import os


class BackendAgent:

    def analyze_project(self, root_path):

        report = []

        for root, dirs, files in os.walk(root_path):

            dirs[:] = [
                d for d in dirs
                if d not in [
                    "venv",
                    "__pycache__",
                    ".git",
                    ".streamlit"
                ]
            ]

            for file in files:

                if file.endswith(".py"):

                    report.append(
                        os.path.join(root, file)
                    )

        return {
            "agent": "BackendAgent",
            "files_found": len(report),
            "files": report
        }

    def analyze_api_modules(self):

        modules = {
            "nikto": False,
            "spiderfoot": False,
            "enum4linux": False,
            "john": False,
            "kubehunter": False
        }

        routes_path = "/home/sentineladmin/sentinel-os/backend/api/routes"

        if not os.path.exists(routes_path):
            return modules

        for file in os.listdir(routes_path):

            if file == "nikto.py":
                modules["nikto"] = True

            elif file == "spiderfoot.py":
                modules["spiderfoot"] = True

            elif file == "enum4linux.py":
                modules["enum4linux"] = True

            elif file == "john.py":
                modules["john"] = True

            elif file == "kubehunter.py":
                modules["kubehunter"] = True

        return modules


    def generate_roadmap(self):

        modules = self.analyze_api_modules()

        roadmap = []

        for module, status in modules.items():

            if not status:
                roadmap.append(module)

        return {
            "completed": [
                m for m, s in modules.items()
                if s
            ],
            "pending": roadmap
        }
