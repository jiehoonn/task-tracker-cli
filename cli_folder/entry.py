import argparse
import json
import datetime
from tabulate import tabulate

# General Commands
def list_tasks(status: str = None):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)
        
        if status is None:
            print(tabulate(data, headers="keys", tablefmt="grid"))
        elif ((status != 'todo') and
            (status != 'in progress') and
            (status != 'done')
        ):
            print(f'"{status}" is not a valid status.')
        else:
            sorted_data = []
            for task in data:
                if task['status'] == status:
                    sorted_data.append(task)
            print(tabulate(sorted_data, headers="keys", tablefmt="grid"))              

    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")

def update_task_ids(data: list):
    for i in range(len(data)):
        if data[i]['id'] != (i + 1):
            data[i]['id'] = i + 1
    return data


def find_next_task_id(data: list):
    if not data:
        return 1
    last_id = data[-1]['id']
    return last_id + 1

# CRUD Functions
def add_task(description: str):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)

        task_id = find_next_task_id(data)

        task = {
            'id': task_id,
            'description': description,
            'status': 'todo',
            'createdAt': str(datetime.datetime.now()),
            'updatedAt': str(datetime.datetime.now()),
        }

        data.append(task)
        data = update_task_ids(data)

        with open(filename, 'w') as task_list:
            json.dump(data, task_list, indent=4)

        print("Successfully added task to task list!")
            
    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")


def delete_task(task_id: int):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)
        
        data = data[:task_id - 1] + data[task_id:]
        data = update_task_ids(data)

        with open(filename, 'w') as task_list:
            json.dump(data, task_list, indent=4)
        
        print("Task deleted successfully!")
    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")


def update_task(task_id: int, new_description: str):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)
        
        for task in data:
            if task['id'] == task_id:
                task['description'] = new_description
                task['updatedAt'] = str(datetime.datetime.now())
        
        with open(filename, 'w') as task_list:
            json.dump(data, task_list, indent=4)
        
        print("Task updated successfully!")
    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")

# Status Functions
def mark_in_progress(task_id: int):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)
        
        data[task_id - 1]['status'] = "in progress"
        data[task_id - 1]['updatedAt'] = str(datetime.datetime.now())

        with open(filename, 'w') as task_list:
            json.dump(data, task_list, indent=4)
        
        print('Task marked as "in progress"!')

    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")
        

def mark_done(task_id: int):
    filename = 'cli_folder/task_list.json'

    try:
        with open(filename, 'r') as task_list:
            data = json.load(task_list)
        
        data[task_id - 1]['status'] = "done"
        data[task_id - 1]['updatedAt'] = str(datetime.datetime.now())

        with open(filename, 'w') as task_list:
            json.dump(data, task_list, indent=4)
        
        print('Task marked as "done"!')

    except FileNotFoundError:
        print(f"Trouble finding your task list! Verify folder structure integrity.")

def cli_entry_point():
    # Create Task List ===============
    default_data = []
    filename = 'cli_folder/task_list.json'

    try:
        # Try to open in read mode ('r')
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError:
        # If the file doesn't exist, create it in write mode ('w')
        print("Initializing task list!")
        with open(filename, 'w') as f:
            json.dump(default_data, f, indent=4)
    
    # Create Argument Parser =========
    parser = argparse.ArgumentParser(
        prog='Task Tracker CLI',
        description='Command Line Interface for tracking your tasks.',
        epilog='Try using any of these commands!'
    )
    subparsers = parser.add_subparsers(dest='command')
    
    # Arguments ======================
    
    # 1. Add task
    parser_add_task = subparsers.add_parser('add', help='Add a task to your task list.')
    parser_add_task.add_argument('description', type=str, help='Description of your task.')

    # 2. Update task
    parser_update_task = subparsers.add_parser('update', help='Update the description of a task.')
    parser_update_task.add_argument('task_id', type=int, help='ID of the task being updated.')
    parser_update_task.add_argument('new_description', type=str, help='New description of updated task.')

    # 3. Delete task
    parser_delete_task = subparsers.add_parser('delete', help='Delete a task from task list.')
    parser_delete_task.add_argument('task_id', type=int, help='ID of task being deleted')

    # 4. Mark "In Progress"
    parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help='Mark a task as "in progress"')
    parser_mark_in_progress.add_argument('task_id', type=int, help='ID of task being marked as "in progress"')

    # 5. Mark "Done"
    parser_mark_done = subparsers.add_parser('mark-done', help='Mark a task as "done"')
    parser_mark_done.add_argument('task_id', type=int, help='ID of task being marked as "done"')

    # 6. List task list
    parser_list_tasks = subparsers.add_parser('list', help='List task list')
    parser_list_tasks.add_argument('-s', '--status', type=str, help='The status of the list you are looking for')

    # Execute Functions ==============
    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.task_id, args.new_description)
    elif args.command == 'delete':
        delete_task(args.task_id)
    elif args.command == 'mark-in-progress':
        mark_in_progress(args.task_id)
    elif args.command == 'mark-done':
        mark_done(args.task_id)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()