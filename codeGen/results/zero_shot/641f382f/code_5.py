import math
from sys import stdin

def find_min_operations(n, arr):
    # Step 3: Check if there is already a 1 in the array.
    if 1 in arr:
        return n - 1
    
    # Step 4: Check if we can create a 1 by finding GCD of adjacent elements.
    for i in range(n - 1):
        if math.gcd(arr[i], arr[i + 1]) == 1:
            return n - 1  # We found a 1, so we can make the whole array 1.
    
    # If we cannot find or create a 1, it's impossible to make all elements equal to 1.
    return -1

# Read input from stdin.
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the minimum number of operations.
print(find_min_operations(n, arr))
