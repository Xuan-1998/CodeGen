import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_operations_to_make_all_elements_one(n, arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return n - 1
    
    # Check if we can get 1 by combining any two adjacent elements
    for i in range(n - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return n - 1
    
    # If we cannot get 1 by combining any two elements, return -1
    return -1

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result to stdout
print(min_operations_to_make_all_elements_one(n, arr))
