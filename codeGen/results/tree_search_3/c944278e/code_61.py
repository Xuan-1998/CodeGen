import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))

dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range((1 << i) - 1, -1, -1):
        if s[i - 1] == (j >> (i - 1)) & 1:
            dp[i][j] = max(dp[i - 1][k] for k in range(j + 1))
        else:
            dp[i][j] = 0

winners = [i for i in range(1 << n) if dp[n][i]]

print(*sorted(winners), sep='\n')
