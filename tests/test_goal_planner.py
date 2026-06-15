from backend.agents.goal_planner import GoalPlanner


def test_goal_planner_creates_create_file_task_from_goal_text():
    planner = GoalPlanner()

    tasks = planner.plan("Create a file at notes.txt with content Hello Sentinel")

    assert tasks == [
        {
            "type": "create_file",
            "path": "notes.txt",
            "content": "Hello Sentinel",
            "goal": "Create a file at notes.txt with content Hello Sentinel",
        }
    ]


def test_goal_planner_creates_command_task_for_shell_goals():
    planner = GoalPlanner()

    tasks = planner.plan("Run the command: ls -la")

    assert tasks == [
        {
            "type": "command",
            "command": "ls -la",
            "goal": "Run the command: ls -la",
        }
    ]
