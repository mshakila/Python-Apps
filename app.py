# To do list App 
tasks = []

def addTask():
    task = input("Please enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the Task list ")

def listTasks():
    if not tasks:
        print("There are currently no tasks.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task #{index}. {task}")
            # Task #2. go home

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # of the task to delete: "))
        if 0 <= taskToDelete <= len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been removed")
        else:
            print(f"Task #{taskToDelete} not found ")
    except:
        print("invalid input")
        

if __name__ == "__main__":
    # create a loop to run the app
    print("Welcome to the To-do-list App !")
    
    while True:
        print("\n")
        print("Please select one option from the following")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        print("\n")
        
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print("invalid input, please try again.")
    print("Goodbye 👋 👋")
