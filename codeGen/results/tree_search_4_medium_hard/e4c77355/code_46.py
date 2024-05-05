import sys

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Initialize DP array with values from base case
dp = [1] * n

# Calculate DP values for each index
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Find the maximum length of the longest increasing subsequence
print(max(dp))
