from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
s = stdin.readline().strip()

dp = [[s] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(k, i), -1, -1):
        if j == k:
            break
        elif dp[i][j] is None or (len(dp[i-1][j-1]) < len(dp[i][j])):
            dp[i][j] = min(dp[i-1][j-1], s[:i])

stdout.write(min(dp[n][k:], default=s, key=len))
