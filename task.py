tasks = []

def display():
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t}")
    print()

while True:
    print("***CHOICE***")
    print("1. Enter task")
    print("2. Delete task")
    print("3. Show tasks")
    print("4. Exit")
    try:
        c = int(input("Enter your choice (1-4): "))
        if c not in range(1, 5):
            print("Please enter a valid choice.")
            continue
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if c == 1:
        add = input("Enter the task:")
        tasks.append(add)
    
    elif c == 2:
        if not tasks:
            print("Task list is empty.")
            continue

        display()
        try:
            idx = int(input("Enter the number of the task to delete: ")) - 1
            if idx in range(0,len(tasks)):
                print(f"Removed task:",tasks.pop(idx))
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif c == 3:
        if not tasks:
            print("No tasks to show.")
        else:
            print("Your tasks:")
            display()
    
    elif c == 4:
        print("Exiting...")
        break
    
    