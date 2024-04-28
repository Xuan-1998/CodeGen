from sys import stdin
from collections import defaultdict

k, n = map(int, stdin.readline().split())
a, b = int(input()), int(input())

dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(n + 1):
        if j == 0:
            dp[i][j] = a
        elif j == 1:
            dp[i][j] = (a ^ b)
        else:
            dp[i][j] = ((dp[i-1][j//2]) * 2) % (10**9 + 7)

print(dp[k][n])
