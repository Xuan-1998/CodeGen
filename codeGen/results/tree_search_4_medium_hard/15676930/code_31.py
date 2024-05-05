import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][:2])
    dp[i][2] = max(dp[i-1][:-1])

print(max(dp[-1]))
