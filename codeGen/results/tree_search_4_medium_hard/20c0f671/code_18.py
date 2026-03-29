from collections import deque

n, m = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = float('inf')
        for k in range(j):
            if books[i - 1][0] <= j and books[i - 1][1] + dp[i - 1][k] < dp[i][j]:
                dp[i][j] = max(dp[i][j], books[i - 1][1] + dp[i - 1][k])

print(min(dp[n]))
