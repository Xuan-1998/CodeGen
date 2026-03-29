import math
import sys

# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the minimum operations to make all elements equal to 1
def min_operations_to_make_ones(n, arr):
    # If there is an element which is already 1, no operations are needed
    if 1 in arr:
        return 0

    # Initialize the minimum operations to a large number
    min_operations = float('inf')

    # Calculate the GCD of each pair of adjacent elements and find the minimum operations
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            # If we find a GCD of 1, update the minimum operations
            if current_gcd == 1:
                min_operations = min(min_operations, j - i)
                break

    # If we haven't found a GCD of 1, it's impossible to make all elements equal to 1
    if min_operations == float('inf'):
        return -1

    return min_operations

# Reading input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output the result to stdout
print(min_operations_to_make_ones(n, arr))
