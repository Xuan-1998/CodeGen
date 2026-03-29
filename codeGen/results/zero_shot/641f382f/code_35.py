import math
import sys

def min_operations_to_make_ones(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return 0
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Find the GCD of all adjacent pairs and the minimum operations
    for i in range(n - 1):
        gcd = math.gcd(arr[i], arr[i + 1])
        if gcd == 1:
            # Count the operations to move the 1 to the beginning and end
            operations = i + (n - 1 - i)
            min_operations = min(min_operations, operations)
    
    # If no GCD of 1 was found, return -1
    if min_operations == float('inf'):
        return -1
    
    return min_operations

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output the result to stdout
print(min_operations_to_make_ones(n, arr))
