import sys
input = sys.stdin.readline

n, t = map(int, input().split())
frac = float(input())

dp = [[0] * (t + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(t + 1):
        if j < t:
            dp[i][j] = max(dp[i - 1][j], int(frac * (10 ** i)) + dp[i - 1][j - 1])
        else:
            dp[i][j] = int(frac * (10 ** i))

print(int(frac * (10 ** n)) + dp[n][t])
