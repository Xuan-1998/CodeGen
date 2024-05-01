import sys

n, m = map(int, input().split())
dp = [[sys.maxsize, -1] for _ in range(n)]

for u, v in [map(int, input().split()) for _ in range(m)]:
    dp[v][0] = min(dp[u][0], 1)
    dp[v][1] = max(dp[u][1], 1)

s, t = map(int, input().split())
k = int(input())

print(minmax[t-1][0], minmax[t-1][1])
