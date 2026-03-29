from math import gcd
from sys import stdin

def find_gcd_of_all_elements(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return 1
    return current_gcd

def find_min_operations(arr):
    if 1 in arr:
        return 0
    gcd_all_elements = find_gcd_of_all_elements(arr)
    if gcd_all_elements > 1:
        return -1
    
    # Count operations to make all elements equal to 1
    operations = 0
    for i in range(len(arr) - 1):
        if gcd(arr[i], arr[i + 1]) == 1:
            operations += 1
    return operations

# Read input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Find and print the minimum number of operations
min_operations = find_min_operations(arr)
print(min_operations)
