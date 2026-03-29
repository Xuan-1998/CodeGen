def max_remaining_element(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the remaining element
    remaining = arr[0]
    
    # Iterate through the sorted array and perform the subtraction
    for i in range(1, n):
        remaining -= arr[i]
    
    return remaining

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:]))

# Get the result
result = max_remaining_element(n, arr)

# Print the result
print(result)

