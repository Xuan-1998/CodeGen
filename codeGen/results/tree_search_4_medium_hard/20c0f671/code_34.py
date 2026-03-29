import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = sys.maxsize
        for k in range(i, -1, -1):
            if j >= books[k][0]:
                dp[i][j] = min(dp[i][j], dp[k-1][j-books[k][0]] + books[k][1])
max_height = 0
for i in range(n, -1, -1):
    max_height = max(max_height, dp[i][m])
print(max_height)
