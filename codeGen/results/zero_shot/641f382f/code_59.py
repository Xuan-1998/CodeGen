from math import gcd
from sys import stdin

def find_min_operations(arr, n):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Check if any pair of adjacent elements has GCD 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i+1]) == 1:
            min_operations = 0
            for j in range(n):
                # Find distance to the nearest pair with GCD 1
                min_operations += min(abs(i-j), abs(i+1-j))
            return min_operations
    
    # If no such pair exists, it's impossible to make all elements 1
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(find_min_operations(arr, n))
