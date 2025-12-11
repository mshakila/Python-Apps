# To do list App 
tasks = []

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
        
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask
        elif choice == "4":
            break
        else:
            print("invalid input, please try again.")
    print("Goodbye !")
