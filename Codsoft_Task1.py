class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def update_task(self, index, updated_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = updated_task
            print(f"Task {index} has been successfully updated")
        else:
            print("Invalid..... not a valid index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task}' deleted from the to-do list.")
        else:
            print("Invalid..... not a valid index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. ....Display tasks.....")
        print("2. ....Add a task.....")
        print("3. ....Update a task.....")
        print("4. ....Delete a task.....")
        print("5. ...Exit....")

        choice = input("Enter your choice between 1 to 5: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter  task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter the task index to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(index, updated_task)
        elif choice == '4':
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
