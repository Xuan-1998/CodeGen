import sys

n, *ws = map(int, input().split())
ws = [w for w in ws]
edges = []
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

dp = [[[[0] * (10**9 + 1) for _ in range(10**9 + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

def dfs(i, j):
    if dp[i][j].pop():
        return
    ws[i] -= j
    for u, v, c in edges:
        if u == i:
            dfs(v, min(ws[v], j + c))
    ws[i] += j

for i in range(1, n + 1):
    if ws[i - 1]:
        dfs(i, ws[i - 1])
print(dp[-1][-1].index(max(dp[-1][-1])))
