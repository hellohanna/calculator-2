"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(numbers):
    """Raise num1 to the power of num and return the value."""
    number_of_numbers = len(numbers)
    my_exponent = numbers[number_of_numbers-1]
    result = 0
    for i in reversed(range(0,len(numbers)-1)):
        result = numbers[i]**my_exponent
        my_exponent = result

    return result


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
