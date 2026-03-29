import math
from sys import stdin

def find_min_operations(n, arr):
    # Check if any element is already 1
    if 1 in arr:
        return n - arr.count(1)

    # Check for pairs with GCD 1
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            # Calculate the number of operations
            operations = 0
            for j in range(n):
                operations += abs(j - i)
            return operations

    # If no such pair exists, return -1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Find and print the minimum number of operations
print(find_min_operations(n, arr))
