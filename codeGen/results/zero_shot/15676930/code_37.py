import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + a[i]
    dp[i][1] = max(dp[i-2][0] if i >= 2 else 0, dp[i-1][1]) + b[i]

print(max(dp[-1]))
