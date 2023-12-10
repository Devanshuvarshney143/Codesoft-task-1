# an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)  
    print("Task added!")  

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks added yet.")  
    else:
        print("Tasks:")
        
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")  

# Function to remove a task based on its index
def remove_task(task_number):
    if 1 <= task_number <= len(tasks): 
        del tasks[task_number - 1]  
        print("Task removed!")  
    else:
        print("Invalid task number.")  

# Loop to run the To-Do List Application 
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Perform actions based on user choice
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)  #call add_task function to add task
    elif choice == '2':
        view_tasks()    #call view_task function to view tasks
    elif choice == '3':
        view_tasks()  
        task_number = int(input("Enter task number to remove: "))
        remove_task(task_number)  #call remove_tasks function to delete tasks
    elif choice == '4':
        print("Goodbye!") 
        break  # Exit the while loop to end the program
    else:
        print("Invalid choice. Please try again.")
