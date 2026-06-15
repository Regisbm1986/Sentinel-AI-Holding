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

        return [
            {
                "type": "command",
                "command": text,
                "goal": text,
            }
        ]
