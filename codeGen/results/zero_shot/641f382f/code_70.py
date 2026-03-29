from math import gcd
from sys import stdin

# Function to find the GCD of the entire array
def find_gcd_of_array(arr):
    array_gcd = arr[0]
    for num in arr[1:]:
        array_gcd = gcd(array_gcd, num)
        if array_gcd == 1:
            return 1
    return array_gcd

# Function to find the minimum operations
def min_operations_to_make_ones(arr):
    array_gcd = find_gcd_of_array(arr)
    if array_gcd > 1:
        return -1
    
    # Find the shortest subarray with a GCD of 1
    n = len(arr)
    min_operations = float('inf')
    for i in range(n):
        current_gcd = arr[i]
        if current_gcd == 1:
            min_operations = min(min_operations, i)
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                min_operations = min(min_operations, j - i)
                break
    
    return min_operations

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(min_operations_to_make_ones(arr))
