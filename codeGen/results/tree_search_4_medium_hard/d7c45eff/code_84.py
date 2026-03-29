from sys import stdin

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for j in range(k+1):
    dp[0][j] = ''

for i in range(1, n+1):
    for j in range(i, k+1):
        if s[i-1] == dp[i-1][j-1][-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[0][j-i] + s[:i]

print(min([dp[n][k]], key=len))
