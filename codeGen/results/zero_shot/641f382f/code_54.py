from math import gcd
import sys

def min_operations_to_make_all_elements_one(n, array):
    # Check if there is already a 1 in the array
    if 1 in array:
        return 0

    # Initialize the minimum operations to a large number
    min_operations = float('inf')

    # Compute the GCD of all pairs of adjacent elements
    for i in range(n - 1):
        current_gcd = gcd(array[i], array[i + 1])

        # If we find a GCD of 1, update the minimum operations
        if current_gcd == 1:
            min_operations = min(min_operations, i + (n - i - 1))
            break

    # If we did not find a GCD of 1, return -1
    if min_operations == float('inf'):
        return -1

    return min_operations

# Read input from stdin
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Output the result to stdout
print(min_operations_to_make_all_elements_one(n, array))
