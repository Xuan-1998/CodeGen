from sys import stdin

n, m = map(int, stdin.readline().split())
nums = [int(x) for x in stdin.readline().split()]

dp = [[False] * m for _ in range(n+1)]

for i in range(m):
    dp[0][i] = True

for i in range(1, n+1):
    for j in range(m):
        if (j >= 0 and (j % m == 0 or any(dp[i-1][k] for k in range(j, i) if j - k * m >= 0))):
            dp[i][j] = True

print(1 if any(dp[n][i] for i in range(m)) else 0)
