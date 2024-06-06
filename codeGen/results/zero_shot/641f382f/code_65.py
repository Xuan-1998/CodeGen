import math
import sys

def find_min_operations(arr):
    # Check for any pair with GCD of 1
    for i in range(len(arr) - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            # If found, return the count of non-1 elements
            return len(arr) - arr.count(1)
    return -1  # If no such pair exists, return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result
print(find_min_operations(arr))
