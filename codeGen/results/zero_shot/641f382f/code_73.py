from math import gcd
from sys import stdin

def min_operations_to_make_ones(n, array):
    # Check if there is already a 1 in the array
    if 1 in array:
        return 0

    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    # Flag to check if it is possible to make all elements 1
    possible = False
    
    # Calculate GCDs and count operations
    for i in range(n):
        current_gcd = array[i]
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, array[j])
            if current_gcd == 1:
                # Update the minimum operations
                min_operations = min(min_operations, j - i)
                possible = True
                break  # No need to check further in this segment
    
    # If it is not possible to make all elements 1, return -1
    if not possible:
        return -1
    
    # Return the minimum operations required
    return min_operations

# Read input from stdin
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().split()))

# Output the result to stdout
print(min_operations_to_make_ones(n, array))
