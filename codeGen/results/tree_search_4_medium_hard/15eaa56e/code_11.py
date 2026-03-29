import sys

n, m = map(int, input().split())
dp = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0 or all(x <= y for x, y in zip(dp[i][:(j-1)], dp[i][j:])):
            dp[i][j] = True

k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    for j in range(m):
        if dp[l-1][j] and dp[r][j]:
            print("Yes")
            sys.exit(0)
print("No")
