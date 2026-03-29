import math
from sys import stdin

def min_operations_to_make_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    # If no 1 is found, check if it is possible to get a 1 via GCD
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i+1]) == 1:
            return 1  # Since we can always make the entire array 1 with one element being 1
    
    # If we cannot find a GCD of 1 between any adjacent elements, it's impossible
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Get the result and print to stdout
print(min_operations_to_make_ones(n, arr))
