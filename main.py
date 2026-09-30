# main.py
# This is the main file that runs the calculator
# It shows the menu, takes input from the user,
# calls the right function and displays the result

from calculator import add, subtract, multiply, divide, modulus, power, square_root
from validator import validate_number


def show_menu():
    """
    Display the list of operations available to the user.
    """
    print("\n" + "=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("  1. Addition          ( + )")
    print("  2. Subtraction       ( - )")
    print("  3. Multiplication    ( * )")
    print("  4. Division          ( / )")
    print("  5. Modulus           ( % )")
    print("  6. Power             ( ^ )")
    print("  7. Square Root       ( √ )")
    print("  0. Exit")
    print("=" * 40)


def get_two_numbers():
    """
    Ask the user to enter two numbers and validate them.
    Returns both numbers as floats.
    """
    a = input("  Enter first number  : ").strip()
    validate_number(a)

    b = input("  Enter second number : ").strip()
    validate_number(b)

    return float(a), float(b)


def get_one_number():
    """
    Ask the user to enter one number and validate it.
    Returns the number as a float.
    """
    a = input("  Enter number : ").strip()
    validate_number(a)
    return float(a)


def display_result(result):
    """
    Print the result in a clean and readable format.
    """
    print(f"\n  Result : {result}")


def run():
    """
    Main function that runs the calculator in a loop.
    The loop continues until the user chooses to exit.
    """
    print("\n  Welcome to the Simple Calculator!")
    print("  Built with Python | Beginner Project\n")

    while True:

        # Step 1: show the menu
        show_menu()

        # Step 2: ask the user to pick an operation
        choice = input("\n  Enter your choice (0-7) : ").strip()

        # Step 3: handle the choice
        try:

            if choice == "1":
                print("\n  --- Addition ---")
                a, b = get_two_numbers()
                display_result(add(a, b))

            elif choice == "2":
                print("\n  --- Subtraction ---")
                a, b = get_two_numbers()
                display_result(subtract(a, b))

            elif choice == "3":
                print("\n  --- Multiplication ---")
                a, b = get_two_numbers()
                display_result(multiply(a, b))

            elif choice == "4":
                print("\n  --- Division ---")
                a, b = get_two_numbers()
                display_result(divide(a, b))

            elif choice == "5":
                print("\n  --- Modulus ---")
                a, b = get_two_numbers()
                display_result(modulus(a, b))

            elif choice == "6":
                print("\n  --- Power ---")
                a, b = get_two_numbers()
                display_result(power(a, b))

            elif choice == "7":
                print("\n  --- Square Root ---")
                a = get_one_number()
                display_result(square_root(a))

            elif choice == "0":
                print("\n  Thank you for using the Simple Calculator!")
                print("  Goodbye!\n")
                break

            else:
                print("\n  Invalid choice. Please enter a number between 0 and 7.")

        except (ValueError, ZeroDivisionError) as e:
            print(f"\n  Error : {e}")

        # Step 4: ask if the user wants to continue
        if choice != "0":
            again = input("\n  Do you want to calculate again? (yes / no) : ").strip().lower()
            if again not in ("yes", "y"):
                print("\n  Thank you for using the Simple Calculator!")
                print("  Goodbye!\n")
                break


if __name__ == "__main__":
    run()