from math import gcd
import sys

# Function to find the minimum number of operations to make all elements equal to 1
def min_operations_to_make_ones(n, arr):
    # If any element is already 1, no operations are needed
    if 1 in arr:
        return 0
    # Check if any adjacent pair has a GCD of 1
    for i in range(n - 1):
        if gcd(arr[i], arr[i+1]) == 1:
            # If yes, the answer is the number of non-1 elements
            return n
    # If no such pair exists, it's impossible to make all elements equal to 1
    return -1

# Read input from stdin
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_ones(n, arr))
