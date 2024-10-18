import datetime

class Task:
    def __init__(self, description, due_date=None, priority="Normal"):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            status = "Completed"
        else:
            status = "Pending"

        return f"Task: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, priority="Normal"):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        print("Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("Your tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            print("Task marked as complete!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
