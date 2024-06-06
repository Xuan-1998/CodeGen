import math
import sys

# Function to find the minimum number of operations required
def min_operations_to_make_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Check if it's possible to get a 1 through GCD
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # We can spread the 1 across the array
    
    # If we cannot obtain a 1, it's impossible to make all elements 1
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(n, arr))
