from math import gcd
from sys import stdin

def find_min_operations(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Initialize the minimum operations to a large number
    min_operations = float('inf')
    
    # Iterate through the array to find the minimum operations
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # Update the minimum operations needed
                min_operations = min(min_operations, j - i)
                break
    
    # If it's impossible to make all elements equal to 1
    if min_operations == float('inf'):
        return -1
    
    return min_operations + n - 1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(find_min_operations(n, arr))
