def task():
    tasks = []
    print("----Welcome To To-Do List----")

    total_task = int(input("Enter How Many Task You Want to Add :"))
    for i in range(1,total_task+1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        print("\nSelect the operation that you have to perform\n")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Task")
        print("5. Exit")

        choice = int(input("Enter Your Choice :"))
        if(choice == 1):
            add = input("Enater Task Name That You Want To Add :")
            tasks.append(add)
            print(f"Task {add} Has Been Successfully Added.")

        elif(choice == 2):
            update = input("Enter The Task Name You Want To Update :")
            if update in tasks:
                update_val = input("Enter New Task :")
                ind = tasks.index(update)
                tasks[ind] = update_val
                print(f"Updated Task {update_val}")

        elif(choice == 3):
            delete = input("Enter The Task Name You Want To Delete :")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"Task {delete} Has Been Deleted.")

        elif(choice == 4):
            print(f"Total Tasks = {tasks}")

        elif(choice == 5):
            print("Closing The To-Do List.")
            break

        else:
            print("Invalid Input")

task()