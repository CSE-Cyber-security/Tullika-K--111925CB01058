
expenses = []

print("===== DAILY EXPENSE TRACKER =====")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "date": date,
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == 2:
        print("\n----- EXPENSE DETAILS -----")

        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print("Date:", expense["date"])
                print("Category:", expense["category"])
                print("Amount: Rs.", expense["amount"])
                print("----------------------")

    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses)
        print("Total Expenses = Rs.", total)

    elif choice == 4:
        print("Thank you for using Daily Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
