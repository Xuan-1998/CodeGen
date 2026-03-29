import sys

def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]
    
    max_nodes = 0
    for edge in edges:
        u, v, t = edge
        if u == i and j >= t:
            max_nodes = max(max_nodes, dfs(v, j-t) + 1)
    
    dp[i][j] = max_nodes
    return max_nodes

n, m, T = map(int, input().split())
dp = [[0]*(T+1) for _ in range(n+1)]
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u-1, v-1, t))
    
print(dfs(0, T), file=sys.stdout)

for i in range(n-1, -1, -1):
    if dp[i][T]:
        print(i+1, file=sys.stdout)
