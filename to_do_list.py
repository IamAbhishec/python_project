import sys
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def complete_task(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task marked as completed")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python to_do_list.py view")
        print("  python to_do_list.py add \"Task name\"")
        print("  python to_do_list.py done <task_number>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "view":
        view_tasks()
    elif command == "add":
        add_task(sys.argv[2])
    elif command == "done":
        complete_task(int(sys.argv[2]) - 1)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
