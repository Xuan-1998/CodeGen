from math import gcd
from sys import stdin

# Function to find the minimum number of operations to make all elements equal to 1
def min_operations_to_make_ones(n, arr):
    # Check if there is already a '1' in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Initialize variables
    min_subarray_length = float('inf')
    
    # Iterate through the array to find the shortest subarray that can produce '1'
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            min_subarray_length = min(min_subarray_length, i)
            break
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                min_subarray_length = min(min_subarray_length, j - i)
                break
    
    # If it's impossible to make all elements '1', return -1
    if min_subarray_length == float('inf'):
        return -1
    
    # Return the minimum number of operations required
    return n + min_subarray_length - 1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Output the result
print(min_operations_to_make_ones(n, arr))
