import sys

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Initialize dp table with zeros
dp = [[1] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if arr[i - 1] > arr[j]:
            dp[i][j] = max(dp[i][j], dp[j][j] + 1)

# Find the length of the longest increasing subsequence (LIS)
max_lis = max(max(row) for row in dp)

print(max_lis)
