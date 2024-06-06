import math
from sys import stdin

def min_operations_to_make_all_elements_one(arr):
    # Check if there's already a 1 in the array
    if 1 in arr:
        return 0

    n = len(arr)
    for i in range(n):
        gcd = arr[i]
        for j in range(i+1, n):
            gcd = math.gcd(gcd, arr[j])
            if gcd == 1:
                # We found a sequence that can be reduced to 1
                # The number of operations is the distance from this sequence to the start or end
                return (j - i) + min(i, n - j - 1)

    # If we couldn't find any sequence that can be reduced to 1, return -1
    return -1

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the result
print(min_operations_to_make_all_elements_one(arr))
