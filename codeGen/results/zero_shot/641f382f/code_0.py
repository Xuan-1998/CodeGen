import math
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_operations_to_make_ones(array):
    # Check if there is already a 1 in the array
    if 1 in array:
        return len(array) - array.count(1)
    
    # Check if it is possible to make a 1 by GCD of any two adjacent elements
    for i in range(len(array) - 1):
        if gcd(array[i], array[i + 1]) == 1:
            return len(array) - 1  # It will take n-1 operations in the worst case
    
    # If we cannot make a 1, then return -1
    return -1

# Read input from stdin
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(array))
