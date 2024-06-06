from math import gcd
import sys

# Function to calculate the GCD of a subarray using a precomputed table
def calculate_gcd(gcd_table, i, j):
    return gcd(gcd_table[i], gcd_table[j])

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Initialize the dp array with a large number
dp = [float('inf')] * (n + 1)
dp[0] = 0

# Precompute GCDs for all subarrays
gcd_table = [0] * n
gcd_table[0] = arr[0]
for i in range(1, n):
    gcd_table[i] = gcd(gcd_table[i-1], arr[i])

# Dynamic programming to fill dp array
for i in range(n):
    for j in range(i, n):
        if calculate_gcd(gcd_table, i, j) == 1:
            dp[j] = min(dp[j], dp[i] + 1)

# Check if it's possible to make all elements equal to 1
if dp[n-1] == float('inf'):
    print(-1)
else:
    print(dp[n-1])
