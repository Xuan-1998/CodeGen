import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 4 for _ in range(n + 1)]

for i in range(3):
    dp[0][i] = a[i]

for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][2], b[i - 1]) + c[i]
    dp[i][1] = max(dp[i - 1][0], a[i - 1]) + c[i]
    dp[i][2] = max(dp[i - 1][1], b[i - 1]) + a[i]
    dp[i][3] = max(dp[i - 1][3], a[i])

print(max(dp[n]))
