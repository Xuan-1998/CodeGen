def max_remaining_element(n, arr):
    # Sort the array
    arr.sort()
    
    # Initialize the result with the first element
    result = arr[0]
    
    # Iterate through the sorted array and perform the operation
    for i in range(1, n):
        result = result - arr[i]
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

# First line is the size of the array
n = int(data[0])

# Second line contains the elements of the array
arr = list(map(int, data[1:n+1]))

# Get the maximum possible value of the remaining element
result = max_remaining_element(n, arr)

# Print the result
print(result)

