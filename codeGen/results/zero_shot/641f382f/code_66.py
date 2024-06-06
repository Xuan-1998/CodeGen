from math import gcd
from sys import stdin

def find_min_operations(n, arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    # Calculate the overall GCD of the array
    overall_gcd = arr[0]
    for num in arr[1:]:
        overall_gcd = gcd(overall_gcd, num)
    
    # If the overall GCD is greater than 1, it's impossible to make all elements 1
    if overall_gcd > 1:
        return -1
    
    # Find the minimum number of operations to make each element 1
    min_operations = float('inf')
    for i in range(n):
        current_gcd = arr[i]
        operations = 0
        for j in range(i-1, -1, -1):
            current_gcd = gcd(current_gcd, arr[j])
            operations += 1
            if current_gcd == 1:
                min_operations = min(min_operations, operations)
                break
    
    return min_operations

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Get the result and print to stdout
print(find_min_operations(n, arr))
