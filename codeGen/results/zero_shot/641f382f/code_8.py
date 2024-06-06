import math
from sys import stdin

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_array(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return 1
    return current_gcd

def min_operations_to_make_ones(arr):
    array_gcd = gcd_of_array(arr)
    if array_gcd > 1:
        return -1
    
    # Since the GCD of the entire array is 1, we can make all elements 1.
    # We need to find the minimum number of operations.
    # This is equivalent to finding the minimum subsequence with GCD 1.
    min_ops = float('inf')
    for i in range(len(arr)):
        current_gcd = arr[i]
        for j in range(i+1, len(arr)):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                # The subsequence from i to j has GCD 1.
                # We need at most j - i operations for this subsequence.
                min_ops = min(min_ops, j - i)
                break
    return min_ops

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Output the minimum number of operations
print(min_operations_to_make_ones(arr))
