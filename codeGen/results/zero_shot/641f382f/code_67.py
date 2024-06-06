from math import gcd
from sys import stdin

def find_min_operations(n, arr):
    # Check if there is a 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Check if there is a pair with GCD equal to 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # In the worst case, we need to perform n-1 operations
    
    # If no such pair exists, return -1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(find_min_operations(n, arr))
