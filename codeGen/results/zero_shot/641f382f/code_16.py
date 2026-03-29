from math import gcd
from sys import stdin

# Function to find the GCD of an array of numbers
def find_gcd_of_array(arr):
    array_gcd = arr[0]
    for num in arr[1:]:
        array_gcd = gcd(array_gcd, num)
        if array_gcd == 1:
            return 1
    return array_gcd

# Function to find the minimum number of operations
def min_operations_to_make_ones(arr):
    array_gcd = find_gcd_of_array(arr)
    if array_gcd > 1:
        return -1
    # Find the minimum number of operations required
    min_operations = float('inf')
    for i in range(len(arr)):
        temp_gcd = arr[i]
        operations = 0
        for j in range(i - 1, -1, -1):
            temp_gcd = gcd(temp_gcd, arr[j])
            operations += 1
            if temp_gcd == 1:
                min_operations = min(min_operations, operations)
                break
    return min_operations

# Reading input
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculating and printing the result
print(min_operations_to_make_ones(arr))
