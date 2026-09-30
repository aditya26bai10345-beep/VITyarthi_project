# validator.py
# This file checks if the input given by the user is valid or not

def validate_number(value):
    """
    Check if the given value can be converted to a number.
    If not, raise an error with a friendly message.
    """
    try:
        float(value)
    except ValueError:
        raise ValueError(f"  Oops! '{value}' is not a valid number. Please enter digits only.")


def validate_division(b):
    """
    Check if the user is trying to divide by zero.
    Division by zero is not allowed in mathematics.
    """
    if float(b) == 0:
        raise ZeroDivisionError("  Oops! You cannot divide by zero. Please enter a non-zero number.")


def validate_sqrt(a):
    """
    Check if the user is trying to find square root of a negative number.
    Square root of a negative number is not a real number.
    """
    if float(a) < 0:
        raise ValueError("  Oops! Square root of a negative number is not possible. Please enter a positive number.")