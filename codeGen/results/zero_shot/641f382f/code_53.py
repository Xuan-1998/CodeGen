import sys
from math import gcd

# Function to find minimum number of operations to make all elements equal to 1
def min_operations_to_make_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Calculate GCD for every pair and try to find a 1
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # Update the minimum operations required
                min_operations = min(min_operations, j - i)
                break
    
    # If we never found a 1, it's not possible to make all elements equal to 1
    if min_operations == float('inf'):
        return -1
    else:
        return min_operations

# Read input from stdin
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

# Get the minimum number of operations and print to stdout
print(min_operations_to_make_ones(n, arr))
