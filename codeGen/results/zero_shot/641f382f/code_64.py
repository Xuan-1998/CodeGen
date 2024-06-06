from math import gcd
from sys import stdin

def min_operations_to_make_ones(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    min_operations = float('inf')
    
    # Iterate through the array to find the minimum operations needed to create a 1
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            # If we find a 1, we can return the index as the number of operations needed
            return i
        
        for j in range(i + 1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # Update the minimum operations if a smaller sequence is found
                min_operations = min(min_operations, j - i)
                break
    
    return min_operations if min_operations != float('inf') else -1

# Read input from stdin
n = int(input())
arr = list(map(int, stdin.readline().split()))

# Process and print the result
print(min_operations_to_make_ones(n, arr))
