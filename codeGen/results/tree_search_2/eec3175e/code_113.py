from sys import stdin

n, m = map(int, stdin.readline().split())
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = True

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j < int(stdin.readline()):
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j % int(stdin.readline())]

print(int(dp[n][m]))
