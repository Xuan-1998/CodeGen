from math import gcd
from sys import stdin

def find_min_operations(n, arr):
    # Check if there is already a 1 in the array.
    if 1 in arr:
        return 0
    
    # Check if we can find a pair with GCD 1.
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            # Count operations needed to propagate the 1 to all elements.
            return (i + 1) + (n - i - 2)
    
    # If no pairs have GCD 1, it's impossible.
    return -1

# Reading input from stdin.
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculating and printing the minimum number of operations.
print(find_min_operations(n, arr))
