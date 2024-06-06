from math import gcd
from sys import stdin

def find_min_operations(arr):
    # If any element is 1, no operations are needed.
    if 1 in arr:
        return 0

    # Check if the GCD of any pair of adjacent elements is 1.
    for i in range(len(arr) - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            # Number of operations is the total number of elements minus 1.
            return len(arr) - 1

    # If we haven't returned yet, it's not possible to make all elements equal to 1.
    return -1

# Read input from stdin.
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Compute and print the result.
print(find_min_operations(arr))
