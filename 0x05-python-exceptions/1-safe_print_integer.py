#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except (TypeError, ValueError):
        return False  # Return False if a TypeError or ValueError occurs

# Example usage:
if __name__ == "__main__":
    result1 = safe_print_integer(123)
    print("Result 1:", result1)  # Output: 123 \n Result 1: True

    result2 = safe_print_integer("abc")
    print("Result 2:", result2)  # Output: Result 2: False

