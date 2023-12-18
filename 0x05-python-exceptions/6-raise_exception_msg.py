#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a NameError with a specified message.

    Args:
        message (str): The message to include in the NameError.

    Raises:
        NameError: Always raises a NameError with the specified message.
    """
    raise NameError(message)
