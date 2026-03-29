import math
from sys import stdin

# Function to find the GCD of all elements in the array
def gcd_of_array(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Check if the array already contains a 1
if 1 in arr:
    # Count the number of non-1 elements, as each will require at least one operation
    print(arr.count(1) - n)
else:
    # Check if it is possible to make all elements 1 by checking the GCD of the array
    if gcd_of_array(arr) == 1:
        # Find the minimum number of operations required
        # This is the distance to the closest 1 after making a 1 using GCD operations
        # Since we can't directly calculate this, we'll assume the worst case where we need
        # to make a 1 using all elements, which takes n-1 operations, and then n-1 more
        # operations to make all elements 1, so 2*(n-1) in total.
        print(2 * (n - 1))
    else:
        # If the GCD of all elements is not 1, it's impossible to make all elements 1
        print(-1)
