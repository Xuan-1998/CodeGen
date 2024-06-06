from math import gcd
import sys

def min_operations_to_make_ones(n, array):
    # Check if there is already a 1 in the array
    if 1 in array:
        return n - array.count(1)
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    for i in range(n):
        current_gcd = array[i]
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, array[j])
            # If the GCD is 1, we can make the entire array 1s
            if current_gcd == 1:
                min_operations = min(min_operations, j - i)
                break
    
    # If it's not possible to make all elements 1, return -1
    if min_operations == float('inf'):
        return -1
    
    return min_operations + n - 1

# Read input from stdin
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Print the result to stdout
print(min_operations_to_make_ones(n, array))
