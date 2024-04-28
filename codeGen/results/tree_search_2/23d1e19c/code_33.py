from collections import defaultdict

def recompute(v, memo):
    if v == t:  # base case
        return [0, 0]
    if (v, memo) in dp:  # memoization
        return dp[(v, memo)]
    
    children = parent[v]  # get all child vertices
    
    min_recomputes = float('inf')
    max_recomputes = 0
    for u in children:
        min_u, max_u = recompute(u, memo)
        min_recomputes = min(min_recomputes, min_u + 1)
        max_recomputes = max(max_recomputes, max_u + 1)
    
    dp[(v, memo)] = [min_recomputes, max_recomputes]
    return dp[(v, memo)]

n, m = map(int, input().split())
parent = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    parent[u].append(v)

k = int(input())
p = list(map(int, input().split()))

print(*recompute(s, {}))
