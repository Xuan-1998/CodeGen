import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
max_points = 0

for i in range(1, n):
    if a[i-1] < a[i]:
        dp[i+1] = max(dp[i], dp[i-1] + 1)
    else:
        dp[i+1] = max(dp[i], dp[i-1])

max_points = dp[-1]
print(max_points)
