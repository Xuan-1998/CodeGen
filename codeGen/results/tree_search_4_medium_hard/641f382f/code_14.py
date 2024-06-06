from math import gcd
from sys import stdin

def find_operations(arr, n):
    # Check if there is an element with GCD 1 with all other elements
    for i in range(n):
        possible = True
        for j in range(n):
            if i != j and gcd(arr[i], arr[j]) != 1:
                possible = False
                break
        if possible:
            return n - 1  # Number of operations required
    return -1  # If no such element exists

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Find and print the result
print(find_operations(arr, n))
