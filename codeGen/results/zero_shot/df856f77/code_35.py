import sys

# Read input from stdin
n = int(input())
arr = [int(x) for x in input().split()]

# Initialize result and operations variables
result = []
operations = 0

# Iterate through the array
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        # If current element is not less than next element, increment operations
        operations += (arr[i] - arr[i+1]) + 1
    else:
        # If current element is less than next element, reset operations
        operations = 0

# Print the result to stdout
print(operations)
