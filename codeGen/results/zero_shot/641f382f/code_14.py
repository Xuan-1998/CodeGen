from math import gcd
import sys

def find_min_operations(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return 0
    
    # Check for any pair with GCD of 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            # Number of operations is the sum of distances to the ends of the array
            return (i + 1) + (n - i - 2)
    
    # If no such pair is found, return -1
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result
print(find_min_operations(n, arr))
