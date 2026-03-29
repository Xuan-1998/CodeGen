from math import gcd
from sys import stdin

# Function to find the minimum number of operations required
def min_operations_to_make_ones(n, arr):
    # Calculate the GCD of all elements
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = gcd(current_gcd, num)
        if current_gcd == 1:
            return n  # The number of operations is equal to the size of the array

    # If GCD of all elements is not 1, it's impossible to make all elements equal to 1
    return -1

# Read input from stdin
n = int(input())
arr = list(map(int, stdin.readline().split()))

# Calculate and print the result
result = min_operations_to_make_ones(n, arr)
print(result)
