# To-Do List Manager with Completion Status

# Initialize an empty list for tasks
tasks = []

def display_tasks():
    """Displays the list of tasks with their completion status."""
    if not tasks:
        print("\nYour to-do list is empty!\n")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "✘"
            print(f"{i}. [{status}] {task['description']}")
    print()

def add_task():
    """Adds a new task to the list."""
    task_description = input("Enter the new task: ")
    tasks.append({'description': task_description, 'completed': False})
    print(f"Task '{task_description}' added successfully!\n")

def update_task():
    """Updates an existing task."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_description = input("Enter the updated task: ")
                tasks[task_num - 1]['description'] = new_description
                print("Task updated successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

def delete_task():
    """Deletes a task from the list."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['description']}' deleted successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

def toggle_completion():
    """Marks a task as completed or pending."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to toggle completion: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = not tasks[task_num - 1]['completed']
                status = "completed" if tasks[task_num - 1]['completed'] else "pending"
                print(f"Task '{tasks[task_num - 1]['description']}' marked as {status}.\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

def to_do_manager():
    """Main function to run the To-Do List Manager."""
    while True:
        print("To-Do List Manager")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Toggle task completion")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            toggle_completion()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

# Run the To-Do List Manager
to_do_manager()
