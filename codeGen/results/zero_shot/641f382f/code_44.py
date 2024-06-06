import math
from sys import stdin

# Function to find the GCD of the entire array
def find_gcd(arr):
    x = arr[0]
    for element in arr[1:]:
        x = math.gcd(x, element)
    return x

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Step 1: Check if there is already a 1 in the array
if 1 in arr:
    print(0)
else:
    # Step 2: Check if it is possible to make all elements equal to 1
    gcd_of_array = find_gcd(arr)
    if gcd_of_array > 1:
        print(-1)
    else:
        # Step 3: Find the minimum number of operations
        for i in range(n - 1):
            # If the GCD of any pair is 1, we can use this pair to make all elements 1
            if math.gcd(arr[i], arr[i + 1]) == 1:
                # The number of operations is the distance from the end of the array
                print(n - 1 - i)
                break
