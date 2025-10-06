"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers together"""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a"""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    print(f"Multiplying {a} × {b}")
    result = a * b
    print(f"Result: {result}")
    return result


def divide(a: Number, b: Number) -> Number:
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    print(f"Dividing {a} ÷ {b}")
    result = a / b
    print(f"Result: {result}")
    return result


# TODO: Students will add power, sqrt functions


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"3 × 4 = {multiply(3, 4)}")
    print(f"10 ÷ 2 = {divide(10, 2)}")
