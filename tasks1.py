tasks = []


def add_task(task_name):
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Task '{task_name}' added.")


def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = '✓' if task['completed'] else '✗'
            print(f"{index}. [{status}] {task['name']}")


def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f"Task '{tasks[task_index - 1]['name']}' marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task['name']}' deleted.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: "))
            complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: "))
            delete_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()