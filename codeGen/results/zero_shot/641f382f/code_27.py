import math
from sys import stdin

# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the minimum number of operations
def min_operations(arr, n):
    # Base case: if any element is 1, no operations needed for that element
    if 1 in arr:
        return 0

    # Initialize the minimum number of operations to a large number
    min_ops = float('inf')

    # Check for each pair if we can make the elements 1 with a single operation
    for i in range(n-1):
        if gcd(arr[i], arr[i+1]) == 1:
            # If yes, update the minimum operations if it is less than the current minimum
            min_ops = min(min_ops, i + (n - i - 2))

    # If it was impossible to make all elements 1, return -1
    if min_ops == float('inf'):
        return -1

    return min_ops

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Call the function and print the result to stdout
print(min_operations(arr, n))
