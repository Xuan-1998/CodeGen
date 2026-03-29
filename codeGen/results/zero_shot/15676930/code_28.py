import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i-1]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i-1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i-1]

print(max(dp[n]))
