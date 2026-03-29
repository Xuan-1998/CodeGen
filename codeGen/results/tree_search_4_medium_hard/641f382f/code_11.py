import math
from sys import stdin

def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def min_operations_to_make_ones(array, n):
    # Check if there is a 1 in the array
    if 1 in array:
        return n - 1
    
    # Compute the GCD of the entire array
    gcd = array[0]
    for i in range(1, n):
        gcd = compute_gcd(gcd, array[i])
    
    # If the GCD of the entire array is not 1, it's impossible
    if gcd != 1:
        return -1
    
    # Find the minimum number of operations to make the GCD of any subarray 1
    for length in range(2, n+1):  # Subarray lengths
        for start in range(n-length+1):  # Subarray starting points
            subarray_gcd = array[start]
            for end in range(start+1, start+length):  # Subarray ending points
                subarray_gcd = compute_gcd(subarray_gcd, array[end])
                if subarray_gcd == 1:
                    return n + length - 2  # n-1 operations plus operations to make subarray GCD 1

    # If we reach here, something went wrong, return -1
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
result = min_operations_to_make_ones(array, n)
print(result)
