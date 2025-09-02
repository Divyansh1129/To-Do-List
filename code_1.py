
from pymongo import MongoClient

# Replace with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')

db = client.todo_db  # Create or connect to a database named "todo_db"
tasks_collection = db.tasks  # Create or connect to a collection named "tasks"

def create_task(description):
    task = {
        'description': description
    }
    result = tasks_collection.insert_one(task)
    print(f'Task created with id: {result.inserted_id}')

def read_tasks():
    tasks = tasks_collection.find()
    print("\nYour To-Do List:")
    for task in tasks:
        print(f"- {task['description']}")

while True:
        print("\n1. Create Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            create_task(description)
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")