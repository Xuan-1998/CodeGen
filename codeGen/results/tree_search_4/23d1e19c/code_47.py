import sys

def recalc_paths(memo, s, t):
    if (s, t) in memo:
        return memo[(s, t)]
    
    min_recom = 0
    max_recom = 0
    
    for p in [p for p in range(1, n+1) if p in path]:
        if p == s:
            continue
        
        if p == t:
            break
        
        new_min_recom = min_recom + 1
        new_max_recom = max_recom + 1
        
        dp[p][t] = recalc_paths(memo, p, t)
        
        new_min_recom = min(new_min_recom, dp[p][t][0])
        new_max_recom = max(new_max_recom, dp[p][t][1])
        
        memo[(s, t)] = (new_min_recom, new_max_recom)
    
    return memo[(s, t)]

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

path = list(map(int, input().split()))
dp = [[(0, 0) for _ in range(n+1)] for _ in range(n+1)]
memo = {}

min_recom, max_recom = recalc_paths(memo, s, t)
print(min_recom, max_recom)
