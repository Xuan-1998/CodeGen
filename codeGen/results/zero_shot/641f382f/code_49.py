import sys
from math import gcd

# Function to calculate the minimum number of operations
def min_operations_to_make_ones(n, arr):
    # If there's already a 1 in the array, no operations are needed
    if 1 in arr:
        return 0
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Check each pair of adjacent elements
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            # If the GCD of any subarray is 1, we can make all elements 1
            if current_gcd == 1:
                # Update the minimum operations needed
                min_operations = min(min_operations, j - i)
                break
    
    # If it's impossible to make all elements 1, return -1
    if min_operations == float('inf'):
        return -1
    
    # Otherwise, return the minimum operations
    return min_operations + n - 1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(n, arr))
