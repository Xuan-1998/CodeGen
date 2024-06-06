from math import gcd
from sys import stdin

def min_operations_to_make_ones(n, arr):
    # If any element is already 1, we don't need any operations.
    if 1 in arr:
        return 0

    # Initialize dp array with a high value
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case

    # Precompute GCDs of all subarrays
    gcd_precompute = [[0] * n for _ in range(n)]
    for i in range(n):
        gcd_precompute[i][i] = arr[i]
        for j in range(i + 1, n):
            gcd_precompute[i][j] = gcd(gcd_precompute[i][j - 1], arr[j])

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(i):
            # Check if there's a pair with GCD of 1 in the subarray arr[j:i]
            if gcd_precompute[j][i - 1] == 1:
                dp[i] = min(dp[i], dp[j] + 1)

    # If it's impossible to make all elements equal to 1, return -1
    return -1 if dp[n] == float('inf') else dp[n]

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Calculate and print the answer
print(min_operations_to_make_ones(n, arr))
