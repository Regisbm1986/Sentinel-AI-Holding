import re


class GoalPlanner:
    """Convert high-level goals into executable Sentinel tasks."""

    CREATE_FILE_PATTERN = re.compile(
        r"^Create a file at\s+(?P<path>[^\s]+)\s+with content\s+(?P<content>.+)$",
        re.IGNORECASE,
    )
    COMMAND_PATTERN = re.compile(
        r"^Run the command:\s*(?P<command>.+)$",
        re.IGNORECASE,
    )
    API_ROUTE_PATTERN = re.compile(
        r"^Create API route for module\s+'(?P<module>[^']+)'\s+in\s+(?P<path>.+)$",
        re.IGNORECASE,
    )

    def plan(self, goal):
        text = goal.strip()

        create_match = self.CREATE_FILE_PATTERN.match(text)
        if create_match:
            return [
                {
                    "type": "create_file",
                    "path": create_match.group("path"),
                    "content": create_match.group("content"),
                    "goal": text,
                }
            ]

        command_match = self.COMMAND_PATTERN.match(text)
        if command_match:
            return [
                {
                    "type": "command",
                    "command": command_match.group("command").strip(),
                    "goal": text,
                }
            ]

        api_route_match = self.API_ROUTE_PATTERN.match(text)
        if api_route_match:
            module = api_route_match.group("module")
            path = api_route_match.group("path").strip()
            content = (
                "from fastapi import APIRouter\n\n"
                "router = APIRouter()\n\n"
                "@router.get(\"/\")\n"
                "def health():\n"
                f'    return {{"module": "{module}", "status": "ok"}}\n'
            )
            return [
                {
                    "type": "create_file",
                    "path": path,
                    "content": content,
                    "goal": text,
                }
            ]

        return [
            {
                "type": "command",
                "command": text,
                "goal": text,
            }
        ]
