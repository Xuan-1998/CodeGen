import math
import sys

# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the minimum operations to make all elements equal to 1
def min_operations(arr, n):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return 0

    # Initialize the minimum operations to a large number
    min_ops = float('inf')
    # Flag to check if it's possible to make all elements equal to 1
    possible = False

    # Check each pair of adjacent elements
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            possible = True
            # Calculate the minimum operations for each element
            ops = 0
            for j in range(n):
                if j < i:
                    ops += i - j
                elif j > i + 1:
                    ops += j - (i + 1)
            min_ops = min(min_ops, ops)

    # If it's not possible, return -1
    if not possible:
        return -1

    return min_ops

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Find and print the minimum number of operations
print(min_operations(arr, n))
