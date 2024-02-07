tasks = []  # List to store tasks

def add_task(task):
  """Adds a new task to the list."""
  tasks.append(task)
  print(f"Task '{task}' added successfully!")

def list_tasks():
  """Lists all tasks in the list."""
  if not tasks:
    print("No tasks in the list yet!")
    return
  
  for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")

def mark_done(task_index):
  """Marks a task as done based on its index."""
  try:
    tasks[task_index - 1] = f"[DONE] {tasks[task_index - 1]}"
    print(f"Task marked as done!")
  except IndexError:
    print("Invalid task index!")

def delete_task(task_index):
  """Deletes a task based on its index."""
  try:
    del tasks[task_index - 1]
    print(f"Task deleted successfully!")
  except IndexError:
    print("Invalid task index!")

def main():
  """Main loop for user interaction."""
  while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      task = input("Enter new task: ")
      add_task(task)
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      list_tasks()
      index = int(input("Enter task number to mark done: "))
      mark_done(index)
    elif choice == '4':
      list_tasks()
      index = int(input("Enter task number to delete: "))
      delete_task(index)
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()