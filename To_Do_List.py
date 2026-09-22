tasks = ["Belajar Python", "Mengerjakan Tugas", "Belajar C/C++"]
running = True

while running:
    print("==== TO DO LIST ====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    print("")
    choice = input("Choose : ")

    if choice == "4":
        running = False
        print("Thank you for using us!")
        print("")
    elif choice == "1":
        print("")
        print("==== TASKS ====")

        for nomor, task in enumerate(tasks, start=1):
            print(f"{nomor}. {task}")
        print("")
    elif choice == "2":
        print("==== ADD TASK ====")
        new_task = input(("Enter your task: "))
        tasks.append((new_task))
        print("Task addded")
        print("")
    elif choice == "3":
        if not tasks:
            print("There are no task to remove")
            print("")
        else:
            print("")
            print("==== REMOVE TASK ====")
            for nomor, task in enumerate(tasks, start=1):
                print(f"{nomor}. {task}")
            remove_task = int(input("Pick one task in number to remove it: "))
            if remove_task > len(tasks) or remove_task < 1:
                print("")
                print("Invalid number, please try again")
                print("")
            else:
                remove_task = remove_task - 1
                tasks.pop(remove_task)
                print("Task removed")
                print("")