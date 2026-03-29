import sys
from math import inf

# Read input array
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Initialize dp table with negative infinity
dp = [inf] * (n + 1)

# Fill up the dp table
for i in range(1, n + 1):
    for j in range(i):
        if arr[j] < arr[i - 1]:
            dp[i] = min(dp[i], dp[j] + 1)

# Print the length of longest increasing subsequence
print(max(dp[1:]))
