import sys
from math import gcd

def min_operations_to_make_ones(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return n - 1

    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Check for each pair if we can obtain a 1
    for i in range(n - 1):
        current_gcd = gcd(arr[i], arr[i + 1])
        if current_gcd == 1:
            # Calculate operations from the start to the position where we found 1
            operations_to_left = i
            # Calculate operations from the position where we found 1 to the end
            operations_to_right = n - i - 2
            # Update the minimum operations if necessary
            min_operations = min(min_operations, operations_to_left + operations_to_right)
    
    # If we never updated min_operations, it's not possible to obtain a 1
    if min_operations == float('inf'):
        return -1
    
    return min_operations + n - 1  # Add n - 1 to merge the 1 across the array

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_operations_to_make_ones(n, arr))
