
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference of two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Returns the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def main():
    print(add(1, 2))
    print(subtract(3, 4))
    print(multiply(5, 6))
    print(divide(7, 8))

