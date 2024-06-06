from math import gcd
from sys import stdin

def min_operations_to_make_ones(n, array):
    # Step 3: Check if there is a 1 or a pair with GCD 1 in the array
    if 1 in array:
        return n - array.count(1)
    for i in range(n - 1):
        if gcd(array[i], array[i + 1]) == 1:
            return n - 1
    return -1

# Reading input
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))

# Output the result
print(min_operations_to_make_ones(n, array))
