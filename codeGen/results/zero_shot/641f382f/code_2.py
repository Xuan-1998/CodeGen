import math
import sys

def find_min_operations(n, arr):
    # Check if there's an element which is already 1
    if 1 in arr:
        return 0

    # Check if there's a pair with GCD 1
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            return 1  # Since we can make the whole array 1 in one operation

    # If no such pair exists, return -1
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Compute and print the result to stdout
print(find_min_operations(n, arr))
