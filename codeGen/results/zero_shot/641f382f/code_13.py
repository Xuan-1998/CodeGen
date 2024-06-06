from math import gcd
from sys import stdin

def find_min_operations(n, arr):
    # Check if there is any element that is already 1
    if 1 in arr:
        return n - 1

    # Check for adjacent pairs with GCD 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1

    # If we haven't found any pair with GCD 1, return -1
    return -1

# Reading input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculating and printing the result
print(find_min_operations(n, arr))
