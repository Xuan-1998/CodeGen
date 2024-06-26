import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], a[i-1])
    dp[i][1] = max(dp[i-1][1], b[i-1] + dp[i-2][0])
    dp[i][2] = max(dp[i-1][2], c[i-1] + dp[i-2][1])

print(max(dp[n]))
