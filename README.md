# Task Tracker CLI

A simple command-line task manager to track your todos.

## Usage
```bash
python task_tracker.py <command> [arguments]
```

## Commands
- `add "Task description"` - Add new task
- `update <id> "New description"` - Update task
- `remove <id>` - Delete task
- `mark-todo <id>` - Mark as todo
- `mark-in-progress <id>` - Mark as in progress
- `mark-done <id>` - Mark as done
- `list` - Show all tasks
- `list done` - Show completed tasks
- `list todo` - Show todo tasks
- `list in-progress` - Show in-progress tasks

## Examples
```bash
python task_tracker.py add "Learn Python"
python task_tracker.py mark-in-progress 1
python task_tracker.py list
python task_tracker.py mark-done 1
```

Built as part of roadmap.sh projects - https://roadmap.sh/projects/task-tracker
