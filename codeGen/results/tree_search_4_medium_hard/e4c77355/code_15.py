import sys

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

# Initialize dp table with 1's (since an individual element is considered a subsequence of length 1)
dp = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if arr[j] < arr[i]:
            dp[i][j] = max(dp[i][j], dp[j][i-1] + 1) if i > 0 else 2

# The final value in the dp table represents the length of the longest increasing subsequence
print(max([max(row) for row in dp]))

