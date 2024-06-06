import math
import sys

def gcd(a, b):
    return math.gcd(a, b)

def min_operations_to_make_ones(n, arr):
    # Check if any element is already 1
    if 1 in arr:
        return 0
    
    # Check if it is possible to make all elements 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # In the worst case, we make each element 1 one by one
    
    # If it's not possible to make all elements 1
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Get the minimum number of operations and print the result
result = min_operations_to_make_ones(n, arr)
print(result)
