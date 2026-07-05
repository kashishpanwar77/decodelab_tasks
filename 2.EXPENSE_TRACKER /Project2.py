expenses= []

def add_expenses():
    try:
        expense_number = int(input("Enter expense number:"))
    except ValueError:
        print("Please enter a valid number:")
        return
    Category = input("Enter category of expense:")
    Amount = int(input("Enter amount of expense:"))
    Description = input("Enter description of expense:")
    Expenses = {
        "Expense Number": expense_number,
        "Category": Category,
        "Amount" : Amount,
        "Description": Description
        }
    expenses.append(Expenses)
    print("Expenses added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found!")
        return
    else:
        for Expenses in expenses:
            print("Expense Number:", Expenses["Expense Number"])
            print("Category:", Expenses["Category"])
            print("Amount:", Expenses["Amount"])
            print("Description:", Expenses["Description"])

def total_expense():
    total = 0
    for Expenses in expenses:
        total += Expenses["Amount"]
    print("Total Expense:", total)

def highest_expense():
    if not expenses:
        print("No expense found!")
        return
    else:
        highest_expense = 0
        highest_number = None
        for Expenses in expenses:
            if highest_expense < Expenses["Amount"]:
                highest_expense = Expenses["Amount"]
                highest_number = Expenses
        print("Expense Number:", highest_number["Expense Number"])
        print("Category:", highest_number["Category"])
        print("Amount:", highest_number["Amount"])
        print("Description:", highest_number["Description"])
    
def delete_expense():
    try:
        expense_number = int(input("Enter Expense number to be deleted:"))
    except ValueError:
        print("Please enter a valid number!")
        return
    for Expenses in expenses:
        if Expenses["Expense Number"] == expense_number:
            expenses.remove(Expenses)
            print("Expense Deleted succesfully!")
            return
        

def count_expenses():
    count = len(expenses)
    print("Total Expenses:", count)


while True:
    print("===EXPENSE TRACKER===")
    print("1.Add Expense\n 2.View Expenses\n 3.Total Expense\n 4.Highest Expense\n 5.Delete Expense\n 6.Count Expenses\n 7.Exit\n")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a valid number!")

    if choice == 1:
        add_expenses()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total_expense()

    elif choice == 4:
        highest_expense()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        count_expenses()

    elif choice == 7:
        print("Exiting Program....")
        break
    else:
        print("Please enter a valid number!")

    
