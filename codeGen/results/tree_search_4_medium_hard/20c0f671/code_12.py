from sys import stdin

n, k = map(int, stdin.readline().split())
books = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    height, thickness = books[i - 1]
    for w in range(k, thickness - 1, -1):
        dp[i][w] = min(dp[i][w], dp[i - 1][w - thickness] + height)

print(min(dp[n]))
