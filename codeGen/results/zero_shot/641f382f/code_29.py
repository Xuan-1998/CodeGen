from math import gcd
from sys import stdin

def find_min_operations(n, array):
    # Step 3: Check if there's already a 1 in the array
    if 1 in array:
        return 0
    
    # Step 5: Check if there's a pair with GCD equal to 1
    for i in range(n - 1):
        if gcd(array[i], array[i + 1]) == 1:
            return 1  # Since we can make the entire array 1 with this pair
    
    # Step 7: If no such pair exists, return -1
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(find_min_operations(n, array))
