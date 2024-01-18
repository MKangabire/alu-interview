#!/usr/bin/python3
"""Module-level docstring."""

def minOperations(n):
    """
    Print the number of operations.

    Parameters:
    - n (int): Target length.

    Returns:
    - tuple: A tuple containing the final string and the number of operations.
    """
    operations = 0
    result = "H"

    while len(result) < n:
        result += result
        operations += 1

    return result, operations

if __name__ == "__main__":
    n = int(input("Enter the target length (n): "))

    final_string, num_operations = minOperations(n)

    if len(final_string) < n:
        print("If n is impossible to achieve, return 0")
        print("Result is:", 0)
    else:
        print("Final string: {}".format(final_string))
        print("Number of operations: {}".format(num
