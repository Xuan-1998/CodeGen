from math import gcd
from sys import stdin

# Function to find the GCD of a subarray
def find_subarray_gcd(arr, start, end):
    current_gcd = arr[start]
    for i in range(start + 1, end + 1):
        current_gcd = gcd(current_gcd, arr[i])
        if current_gcd == 1:
            return 1
    return current_gcd

# Function to find the minimum operations to make all elements 1
def min_operations_to_make_ones(arr, n):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    min_subarray_length = float('inf')
    
    # Find the shortest subarray with GCD 1
    for i in range(n):
        for j in range(i, n):
            if find_subarray_gcd(arr, i, j) == 1:
                min_subarray_length = min(min_subarray_length, j - i + 1)
    
    # If no such subarray exists, return -1
    if min_subarray_length == float('inf'):
        return -1
    
    # The number of operations is the array length minus the shortest subarray length
    return n - min_subarray_length

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Output the minimum number of operations
print(min_operations_to_make_ones(arr, n))
