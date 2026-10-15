expenses = []


def show_menu():
    print()
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("q. Quit")


def add_expense():
    description = input("What did you spend on? ").strip()
    if description == "":
        print("Description cannot be empty. Nothing was saved.")
        return

    amount_text = input("How much (in naira)? ")
    try:
        amount = float(amount_text)
    except ValueError:
        print("That is not a number. Nothing was saved.")
        return

    if amount <= 0:
        print("Amount must be more than 0. Nothing was saved.")
        return

    expense = {"description": description, "amount": amount}
    expenses.append(expense)
    print("Expense saved.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet")
        return

    number = 1
    for expense in expenses:
        print(f"{number}. {expense['description']} - ₦{expense['amount']:.2f}")
        number = number + 1


def show_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print(f"Total: ₦{total:.2f}")


while True:
    show_menu()
    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3 or q.")