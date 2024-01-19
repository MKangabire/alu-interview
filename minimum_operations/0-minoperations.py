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
    if n <= 1:
        return 0
    for i in range(2, n+1):
        if (n % i) == 0:
            next_n = n // i
            total_ops = i
            break
    return total_ops + minOperations(next_n)
