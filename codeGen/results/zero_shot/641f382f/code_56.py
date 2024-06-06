from math import gcd
from sys import stdin

def min_operations_to_make_all_elements_one(arr):
    # Check if any element is already 1
    if 1 in arr:
        return 0
    
    # Check if it is possible to make all elements 1
    for i in range(len(arr) - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return 1
    
    # If no adjacent elements have GCD of 1, check non-adjacent pairs
    for i in range(len(arr)):
        for j in range(i+2, len(arr)):
            if gcd(arr[i], arr[j]) == 1:
                # The number of operations needed will be equal to the distance between the elements minus 1
                return j - i - 1
    
    # If no pair has GCD of 1, it's impossible to make all elements 1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(min_operations_to_make_all_elements_one(arr))
