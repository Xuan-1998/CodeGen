import sys
from math import gcd

def find_min_operations(arr):
    # First, check if there's already a 1 in the array.
    if 1 in arr:
        return n - arr.count(1)
    
    # Check for pairs with GCD 1.
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # We can make all elements 1 in n-1 operations
    
    # If we reach this point, it's impossible to make all elements 1.
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
result = find_min_operations(arr)
print(result)
