#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        The real number of elements printed.
    """
    printed_count = 0  # Initialize a counter for the printed elements

    # Iterate through the range of x
    for i in range(x):
        try:
            # Attempt to print the current element from the list
            print("{}".format(my_list[i]), end="")
            printed_count += 1  # Increment the counter if printing is successful

        except IndexError:
            # Break out of the loop if the index is out of range
            break

    print("")  # Print a newline after displaying the elements
    return printed_count  # Return the count of successfully printed elements

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

