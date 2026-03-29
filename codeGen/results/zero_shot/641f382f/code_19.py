from math import gcd
from sys import stdin

def find_min_operations(arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return arr.index(1)
    
    # Check if it is possible to obtain a 1 by taking GCDs
    for i in range(len(arr) - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return i
    
    # If it is not possible to make any element 1, return -1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Get the result and print it
result = find_min_operations(arr)
print(result)
