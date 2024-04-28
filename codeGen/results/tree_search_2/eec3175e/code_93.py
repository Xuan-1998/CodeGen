code
from sys import stdin

n, m = map(int, stdin.readline().split())
dp = [[0] * m for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(m):
        if (j + int(stdin.readline())) % m == 0:
            dp[i][j] = 1
        elif dp[i-1][j]:
            dp[i][j] = 1

print(1) if dp[n].index(max(dp[n])) % m == 0 else print(0)
