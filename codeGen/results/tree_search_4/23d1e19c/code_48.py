from collections import defaultdict

def dfs(u, dp):
    if u == t:
        return 0, 0
    min_recom = float('inf')
    max_recom = -float('inf')
    for v in neighbors[u]:
        if not (v[1], v[0]) in path:  # Check if the edge is part of the fixed path
            min_v, max_v = dfs(v, dp)
            min_recom = min(min_recom, min_v + 1)
            max_recom = max(max_recom, max_v + 1)
    return min_recom, max_recom

n, m = map(int, input().split())
neighbors = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    neighbors[u].append((v, True))
path = list(map(int, input().split()))
s, t = path[0], path[-1]

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[s][t] = (0, 0)
min_recom, max_recom = dfs(s, dp)

print(min_recom, max_recom)
