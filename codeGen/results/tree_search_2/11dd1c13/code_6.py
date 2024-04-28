from sys import stdin, maxsize

n = int(stdin.readline())
grid = [[int(x) for x in stdin.readline().split()] for _ in range(n)]

dp = [[maxsize] * n for _ in range(n)]
for i in reversed(range(n)):
    dp[i][0] = min(dp[j][0] + grid[i][0] for j in range(i, n))

for k in range(1, n):
    for i in reversed(range(n-k)):
        for j in range(k):
            dp[i][k] = min(dp[x][j] + grid[i+k-1][j] for x in range(i, n-k))
        if k > 0:
            dp[0][k] = min(dp[j][k-1] + grid[0][k-1] for j in range(1, k))

print(min(dp[0]))

