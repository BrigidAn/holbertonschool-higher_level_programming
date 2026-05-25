#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format()

    Returns:
        True if value is an integer and printed correctly
        False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
