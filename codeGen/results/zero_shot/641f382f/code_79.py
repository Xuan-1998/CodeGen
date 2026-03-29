from math import gcd
from sys import stdin

def min_operations_to_make_all_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0

    # Initialize the minimum operations to a large number
    min_operations = float('inf')

    # Compute GCD of all pairs and find minimum operations to make an element 1
    for i in range(n - 1):
        current_gcd = arr[i]
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # We found a pair that can be reduced to 1
                # The operations needed are the distance between the elements
                min_operations = min(min_operations, j - i)
                break  # No need to continue once we found a 1

    # If it is impossible to make any element 1, return -1
    if min_operations == float('inf'):
        return -1

    # Otherwise, return the total number of operations needed
    # Which is (n - 1) to make all elements equal to the element that became 1
    # Plus the minimum operations to make at least one element 1
    return (n - 1) + min_operations

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Print the result to stdout
print(min_operations_to_make_all_ones(n, arr))
