# calculator.py
# This file contains all the arithmetic operations of the calculator
# Each operation is written as a separate function

import math
from validator import validate_division, validate_sqrt


def add(a, b):
    """
    Add two numbers and return the result.
    Example: add(5, 3) returns 8
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first and return the result.
    Example: subtract(10, 4) returns 6
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers and return the result.
    Example: multiply(3, 4) returns 12
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second and return the result.
    Raises an error if the second number is zero.
    Example: divide(10, 2) returns 5.0
    """
    validate_division(b)
    return a / b


def modulus(a, b):
    """
    Find the remainder when first number is divided by second.
    Example: modulus(10, 3) returns 1
    """
    validate_division(b)
    return a % b


def power(a, b):
    """
    Raise the first number to the power of the second number.
    Example: power(2, 3) returns 8
    """
    return a ** b


def square_root(a):
    """
    Find the square root of a number.
    Raises an error if the number is negative.
    Example: square_root(16) returns 4.0
    """
    validate_sqrt(a)
    return math.sqrt(a)