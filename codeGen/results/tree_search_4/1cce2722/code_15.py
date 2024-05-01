import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(sum(a) + 1)]

for i in range(n):
    sum_i = sum(a[:i+1])
    dp[sum_i][i+1] = max(dp[sum_i-1][i] if i > 0 else 1, dp[sum_i][i-1] if i > 0 and i > 0 else 0) + (n - i)

max_points = 0
for i in range(n):
    sum_i = sum(a[:i+1])
    max_points = max(max_points, dp[sum_i][i+1])

print(max_points)
