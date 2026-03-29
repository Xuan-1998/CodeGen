===BEGIN CODE===
from sys import stdin

n = int(stdin.readline())
w = list(map(int, stdin.readline().split()))
dp = [[0] * (10**9 + 1) for _ in range(n)]

for i in range(1, n):
    u, v, c = map(int, stdin.readline().split())
    dp[i][max(w[u-1]-c, 0)] = max(dp[i-1][j-c] for j in range(max(w[u-1], w[v-1])-c+1) if j >= w[u-1])
    for j in range(10**9 + 1):
        dp[i][j] = max(dp[i][j], dp[i-1][min(j+w[i-1]-w[u-1], w[u-1])])

print(max(dp[-1]))
===END CODE===
