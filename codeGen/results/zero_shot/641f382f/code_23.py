import math
import sys

def find_operations(n, array):
    # Check if there is at least one pair of adjacent elements with GCD equal to 1
    for i in range(n - 1):
        if math.gcd(array[i], array[i + 1]) == 1:
            # If there is such a pair, the answer is the number of elements minus 1
            return n - 1
    # If no such pair exists, it's impossible to make all elements equal to 1
    return -1

# Read input from stdin
n = int(input())
array = list(map(int, input().split()))

# Find the minimum number of operations required
result = find_operations(n, array)

# Print the result to stdout
print(result)
