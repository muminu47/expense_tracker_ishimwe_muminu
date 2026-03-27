expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary (Total + Highest)")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        type_ = input("Enter expense type: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "name": name,
            "type": type_,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\n--- All Expenses ---")
            for exp in expenses:
                print("Name:", exp["name"])
                print("Type:", exp["type"])
                print("Amount:", exp["amount"])
                print("------------------")

    elif choice == "3":
        if not expenses:
            print("No expenses to summarize.")
        else:
            total = 0
            highest = expenses[0]

            for exp in expenses:
                total += exp["amount"]
                if exp["amount"] > highest["amount"]:
                    highest = exp

            print("\n--- Expense Summary ---")
            print("Total Expenses:", total)
            print("Highest Expense:")
            print("Name:", highest["name"])
            print("Type:", highest["type"])
            print("Amount:", highest["amount"])

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")