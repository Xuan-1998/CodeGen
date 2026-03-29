import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 2 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + a[i]
    dp[i][1] = dp[i-1][0]

print(dp[n][0])
