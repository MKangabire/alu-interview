#!/usr/bin/python3
"""rain.py"""


def calculate_water(arr, n):
    """calculates the maximum size of the walls"""
    if not arr:
	return 0

    max_size = 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    for i in range(1, n - 1):
        max_size += max(0, min(left_max[i], right_max[i]) - arr[i])

    return max_size


def rain(walls):
    """calculates the rain retained acording to the len of walls"""
    water_consumed = calculate_water(walls, len(walls))
    return water_consumed
