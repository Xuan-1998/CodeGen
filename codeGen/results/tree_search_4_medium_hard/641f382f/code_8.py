from math import gcd
from sys import stdin

def compute_gcd_of_subarrays(arr):
    n = len(arr)
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                return j - i
    return -1

def min_operations_to_make_all_elements_one(arr):
    # If any element is already 1, we can make the entire array 1 in n-1 operations.
    if 1 in arr:
        return len(arr) - 1
    
    # If no element is 1, we look for the smallest subarray with GCD 1.
    min_subarray_gcd_1 = compute_gcd_of_subarrays(arr)
    
    # If we found a subarray with GCD 1, the result is the length of the array
    # minus the length of the subarray plus the length of the subarray - 1.
    if min_subarray_gcd_1 != -1:
        return len(arr) - min_subarray_gcd_1 + (min_subarray_gcd_1 - 1)
    
    # If it's not possible to make all elements equal to 1, return -1.
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Compute and print the result
print(min_operations_to_make_all_elements_one(arr))
