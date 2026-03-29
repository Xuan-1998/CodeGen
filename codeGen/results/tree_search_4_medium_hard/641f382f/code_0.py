from math import gcd
from functools import reduce
import sys

def find_gcd_of_array(arr):
    return reduce(gcd, arr)

def min_operations_to_make_all_ones(arr):
    # Calculate the gcd of the entire array
    gcd_of_array = find_gcd_of_array(arr)
    
    # If the gcd is 1, return the minimum number of operations required
    if gcd_of_array == 1:
        return len(arr) - 1
    # If the gcd is greater than 1, it is impossible to make all elements equal to 1
    else:
        return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_operations_to_make_all_ones(arr))
