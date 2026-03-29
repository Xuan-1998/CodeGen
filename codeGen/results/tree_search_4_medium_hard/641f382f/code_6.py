from math import gcd
import sys

def min_operations_to_make_ones(n, arr):
    # Check if the array already contains a 1
    if 1 in arr:
        return 0
    
    # Iterate over the array and check for any pair with GCD equal to 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # If such a pair is found, return n - 1
    
    return -1  # If no such pair is found, return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(n, arr))
