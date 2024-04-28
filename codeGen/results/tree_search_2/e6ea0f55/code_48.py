import sys

n, k = map(int, input().split())
nums = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n)]

for i in range(k + 1):
    dp[0][i] = nums[0]

for i in range(1, n):
    for j in range(min(i, k) + 1):
        dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][k])

print(max(dp[-1]))
