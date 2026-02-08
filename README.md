# Task Tracker CLI

A simple command-line interface (CLI) application for managing your tasks. Built with Python, it allows you to add, update, delete, and track the status of your tasks directly from the terminal.

## Features

- **Add tasks** with automatic ID assignment
- **Update** task descriptions
- **Delete** tasks from your list
- **Track status** with three states: `todo`, `in progress`, and `done`
- **List tasks** with optional filtering by status
- **Pretty table output** using tabulate
- **Persistent storage** via JSON file
- **Automatic timestamps** for creation and updates

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd task-tracker-cli
```

2. Install the package:
```bash
pip install -e .
```

This will install the CLI tool as `task-cli` and make it available globally.

## Usage

### Add a task
```bash
task-cli add "Buy groceries"
```

### List all tasks
```bash
task-cli list
```

### List tasks by status
```bash
task-cli list --status todo
task-cli list --status "in progress"
task-cli list --status done
```

### Update a task
```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Mark task as in-progress
```bash
task-cli mark-in-progress 1
```

### Mark task as done
```bash
task-cli mark-done 1
```

### Delete a task
```bash
task-cli delete 1
```

## Data Storage

Tasks are stored in `cli_folder/task_list.json` with the following structure:
```json
{
    "id": 1,
    "description": "Task description",
    "status": "todo",
    "createdAt": "2026-02-07 23:15:36.146469",
    "updatedAt": "2026-02-07 23:15:36.146479"
}
```

## Requirements

- Python 3.x
- tabulate

## Author

Jiehoon Lee (jiehoonn@bu.edu)
