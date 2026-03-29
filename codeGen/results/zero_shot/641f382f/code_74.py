import math
import sys

def find_min_operations(arr):
    # Check if there is already a 1 in the array.
    if 1 in arr:
        return 0
    
    # Initialize the minimum length to a large value.
    min_length = float('inf')
    
    # Iterate over the array to find the shortest subarray with GCD 1.
    for i in range(len(arr) - 1):
        current_gcd = arr[i]
        for j in range(i + 1, len(arr)):
            current_gcd = math.gcd(current_gcd, arr[j])
            if current_gcd == 1:
                min_length = min(min_length, j - i)
                break
    
    # If no such subarray is found, it's impossible to make all elements equal to 1.
    if min_length == float('inf'):
        return -1
    
    # The number of operations is the length of the subarray minus 1.
    return min_length - 1

# Read input from stdin.
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Compute and print the result.
print(find_min_operations(arr))
