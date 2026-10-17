def show_menu():
    print()
    print("=== Calculator ===")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")
    print("q  Quit")


def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2


while True:
    show_menu()

    choice = input("Choose an option: ").strip().lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in ("+", "-", "*", "/"):
        print("Unsupported choice. Please pick +, -, *, / or q.")
        continue

    try:
        num1 = float(input("Enter first number: ").strip())
        num2 = float(input("Enter second number: ").strip())
    except ValueError:
        print("That is not a valid number. Please try again.")
        continue
