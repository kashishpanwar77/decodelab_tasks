my_tasks = []


def load_task():
    try:
        with open("demo.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    my_tasks.append(task)
    except FileNotFoundError:
        pass


def save_tasks():
    with open("demo.txt", "w") as file:
        for task in my_tasks:
            file.write(task+"\n")


def add_tasks():
    task = input("Enter your task:").strip()
    if task not in my_tasks:
        my_tasks.append(task)
        print(task)
        print(" Total Tasks:", len(my_tasks))
        save_tasks()
    else:
        print("Task already exists")


def view_task():
    if len(my_tasks) == 0:
        print("No task found!")
        return
    else:
        print("----TASKS-----")
        for i, task in enumerate(my_tasks, start=1):
            print(f"{i}.{task}")


def search_task():
    task = (input("Enter task number to search:"))
    if task in my_tasks:
        print("Task exist!")
    else:
        print("Task not found!")


def delete_task():
    try:
        task_number = int(input("Enter task number to delete:"))
        if 1 <= task_number <= len(my_tasks):
            deleted_task = my_tasks.pop(task_number - 1)
            print(f"{deleted_task} deleted successfuly")
            save_tasks()
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid task number")


while True:
    print("------TO DO LIST------")
    print("1.Add Task\n 2.View Task\n 3.Search Task\n 4.Delete Task\n 5.Exit\n")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a number")
        continue
    if choice == 1:
        print("Add task selected")
        add_tasks()
    elif choice == 2:
        print("View task selected")
        view_task()
    elif choice == 3:
        print("Serach task selected")
        search_task()
    elif choice == 4:
        print("Delete task selected")
        delete_task()
    elif choice == 5:
        print("Exiting........")
        print("Program exists succesfully!")
        break
    else:
        print("Invalid choice")
