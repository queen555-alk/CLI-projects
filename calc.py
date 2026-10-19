import math


def show_menu():
    print()
    print("=== Calculator ===")
    print("+  Add")
    print("-  Subtract")
    print("*  Multiply")
    print("/  Divide")
    print("q  Quit")


def read_number(prompt):
    """Keep asking until the user types a valid, finite number."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("That is not a valid number. Please try again.")
            continue
        # ensures the number is between + or - 0
        if not math.isfinite(value):
            print("Please enter a normal number (not inf or nan).")
            continue

        return value


def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("+", "-", "*", "/"):
            print("Unsupported choice. Please pick +, -, *, / or q.")
            continue

        num1 = read_number("Enter first number: ")
        num2 = read_number("Enter second number: ")

        if choice == "/" and num2 == 0:
            print("You cannot divide by zero.")
            continue

        result = calculate(num1, choice, num2)
        print(f"Result: {num1} {choice} {num2} = {result}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
