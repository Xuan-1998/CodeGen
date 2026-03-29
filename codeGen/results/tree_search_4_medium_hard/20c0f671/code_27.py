import sys

n, jmax = map(int, input().split())
books = []
for _ in range(n):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

dp = [[0] * (jmax + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(jmax + 1):
        if books[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            min_height = sys.maxsize
            for k in range(min(j, jmax), -1, -1):
                if k >= books[i-1][0]:
                    height = dp[i-1][k-1] + books[i-1][1]
                    min_height = min(min_height, height)
            dp[i][j] = min_height

print(dp[n][jmax])
