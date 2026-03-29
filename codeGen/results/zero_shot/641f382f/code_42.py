from math import gcd
from sys import stdin, stdout

def min_operations_to_make_all_elements_one(arr):
    # Check if there is already a 1 in the array
    if 1 in arr:
        return 0
    
    # Check if it is possible to make all elements equal to 1
    for i in range(len(arr) - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            return 1  # Since we can always make the entire array 1 with at least one pair having GCD 1
    
    # If no pair of adjacent elements have GCD 1, it's impossible
    return -1

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
result = min_operations_to_make_all_elements_one(arr)
stdout.write(str(result) + '\n')
