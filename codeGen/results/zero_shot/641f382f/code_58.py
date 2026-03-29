import math
from sys import stdin, stdout

def min_operations_to_make_ones(n, arr):
    # If any element is 1, no operations are needed
    if 1 in arr:
        return 0
    
    # Check if there is a pair with GCD 1
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            break
    else:
        # If no such pair exists, it's impossible
        return -1
    
    # Find the minimum number of operations
    min_ops = 0
    for i in range(n):
        current = arr[i]
        ops = 0
        while current != 1:
            for j in range(i - ops, i + 1):
                current = math.gcd(current, arr[j])
            ops += 1
        min_ops += ops - 1  # Subtract one because we counted the first element twice
    return min_ops

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Compute and print the result
result = min_operations_to_make_ones(n, arr)
stdout.write(str(result) + '\n')
