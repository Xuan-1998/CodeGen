from sys import stdin

m, n = map(int, stdin.readline().split())
dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    dp[i][0] = int(stdin.readline())

for j in range(n):
    dp[0][j] = int(stdin.readline())

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + int(stdin.readline())

print(dp[m-1][n-1])
