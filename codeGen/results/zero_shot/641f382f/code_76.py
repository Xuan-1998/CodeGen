import sys
from math import gcd

def min_operations_to_make_ones(n, array):
    # Check if there is already a 1 in the array.
    if 1 in array:
        return 0

    # Initialize the minimum operations to a large number.
    min_operations = float('inf')
    for i in range(n):
        current_gcd = array[i]
        if current_gcd == 1:
            return 0  # We found a 1, no operations needed.
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, array[j])
            if current_gcd == 1:
                # The number of operations needed is the distance between the two elements.
                min_operations = min(min_operations, j - i)
                break

    return -1 if min_operations == float('inf') else min_operations

# Read input from stdin.
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Calculate and print the result to stdout.
print(min_operations_to_make_ones(n, array))
