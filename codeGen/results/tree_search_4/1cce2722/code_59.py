from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

dp = [[0]*(105+1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, 106):
        if a[i-1] == k:
            dp[i][k] = dp[i-1][k]
        else:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-1] + 2, dp[i-1][k+1] + 2)

print(max(dp[n]))
