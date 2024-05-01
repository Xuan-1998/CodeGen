import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (2 * n) for _ in range(n)]

for i in range(1, n - 1):
    # Consider all possible choices of deleting elements within the block
    for j in range(i - 1, i + 2):
        # Update the DP table accordingly
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] if j > 0 else 0) + dp[i-1][j+1] if j < n-1 else 0)

print(max(dp[-1]))
