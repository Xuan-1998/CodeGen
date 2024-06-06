import math
from sys import stdin

# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the minimum operations to make all elements equal to 1
def min_operations_to_make_ones(n, arr):
    # If there's already a 1 in the array, no need to perform any operations
    if 1 in arr:
        return n - arr.count(1)
    
    # Find the GCD of all elements in the array
    overall_gcd = arr[0]
    for num in arr[1:]:
        overall_gcd = gcd(overall_gcd, num)
        if overall_gcd == 1:
            break
    
    # If the GCD of all elements is not 1, it's not possible to make all elements equal to 1
    if overall_gcd != 1:
        return -1
    
    # Find the minimum number of operations needed for each element to become 1
    min_ops = float('inf')
    for i in range(n):
        local_gcd = arr[i]
        ops = 0
        for j in range(i + 1, n):
            local_gcd = gcd(local_gcd, arr[j])
            ops += 1
            if local_gcd == 1:
                min_ops = min(min_ops, ops)
                break
    
    # Return the minimum operations required
    return min_ops + n - 1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Print the result to stdout
print(min_operations_to_make_ones(n, arr))
