import sys

n = int(sys.stdin.readline().strip())
commands = list(sys.stdin.readline().strip())

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(min(i, n)+1):
        if commands[i-1] == 'F':
            dp[i][j] = max(dp[i-1][k-1] + 1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][n])
