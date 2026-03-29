import math
from sys import stdin

def find_min_operations(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return 0
    
    # Check if it's possible to make all elements 1
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i+1]) == 1:
            return 1  # It's possible to make all elements 1 with at least one operation
    
    # If we haven't returned yet, it's impossible to make all elements 1
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Compute and print the result
print(find_min_operations(n, arr))
