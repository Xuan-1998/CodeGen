import sys
from math import gcd

def find_min_operations(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0

    # Initialize the length of the shortest subarray with GCD 1 to infinity
    shortest_subarray_len = float('inf')

    # Iterate over all possible subarrays
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            shortest_subarray_len = 1
            break
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # Update the length of the shortest subarray with GCD 1
                shortest_subarray_len = min(shortest_subarray_len, j - i + 1)
                break

    # If there is no subarray with GCD 1, we return -1
    if shortest_subarray_len == float('inf'):
        return -1

    # The minimum number of operations is the length of the array minus
    # the length of the shortest subarray with GCD 1
    return n - shortest_subarray_len

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(find_min_operations(n, arr))
