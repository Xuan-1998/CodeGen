import sys

n, *ws = map(int, input().split())
ws = list(zip(*[iter(ws)]*n))
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

dp = [[0]*10001 for _ in range(n+1)]

def dfs(i, j):
    if i == n: return j
    if dp[i][j] > 0: return dp[i][j]
    for u, v, c in roads:
        if u == i:
            dp[i][j] = max(dp[i][j], dfs(v, min(j+ws[v-1], ws[v-1])) - c)
    return dp[i][j]

print(max(dfs(i, w) for i, w in enumerate(ws)))
