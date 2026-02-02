#!/usr/bin/env python3

import os
import json
import sys
from datetime import datetime, timezone

FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.json")

# Create file if not exists
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        json.dump([], f)

def read_tasks():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def write_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)

def now():
    return datetime.now(timezone.utc).isoformat()

def generate_id(tasks):
    return max([t["id"] for t in tasks], default=0) + 1

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

# ---------------- COMMANDS ----------------

def add_task(description):
    tasks = read_tasks()
    task_id = generate_id(tasks)

    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now()
    }

    tasks.append(task)
    write_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["description"] = description
    task["updatedAt"] = now()
    write_tasks(tasks)
    print(f"Task updated successfully (ID: {task_id})")

def delete_task(task_id):
    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    tasks.remove(task)
    write_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")

def update_status(task_id, status):
    tasks = read_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["status"] = status
    task["updatedAt"] = now()
    write_tasks(tasks)
    print(f"Task status updated successfully (ID: {task_id})")

def list_tasks(status=None):
    tasks = read_tasks()

    if status:
        tasks = [t for t in tasks if t["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(f'{t["id"]}. [{t["status"]}] {t["description"]}')

# ---------------- CLI ----------------

def handle_arguments():
    args = sys.argv[1:]

    if not args:
        print("Usage: task-cli <command>")
        return

    command = args[0]

    if command == "add":
        add_task(args[1])

    elif command == "update":
        update_task(int(args[1]), args[2])

    elif command == "delete":
        delete_task(int(args[1]))

    elif command == "mark-in-progress":
        update_status(int(args[1]), "in-progress")

    elif command == "mark-done":
        update_status(int(args[1]), "done")

    elif command == "list":
        status = args[1] if len(args) > 1 else None
        list_tasks(status)

    else:
        print("Unknown command.")

if __name__ == "__main__":
    handle_arguments()
