def maximize_remaining_element(n, arr):
    if n == 1:
        return arr[0]

    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize result with the largest element
    result = arr[0]
    
    # Iterate through the rest of the array
    for i in range(1, n):
        result -= arr[i]
    
    return result

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:]))

# Calculate and print the result
print(maximize_remaining_element(n, arr))

