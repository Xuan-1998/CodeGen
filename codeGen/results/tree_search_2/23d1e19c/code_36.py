import heapq

def recompute_path(i, j):
    if (i, j) in dp:
        return dp[(i, j)]
    
    min_recomputations = float('inf')
    max_recomputations = 0
    
    for neighbor in graph[i]:
        if neighbor == t:  # We've reached the destination
            continue
        
        recomputations = recompute_path(neighbor, j+1)
        min_recomputations = min(min_recomputations, recomputations[0])
        max_recomputations = max(max_recomputations, recomputations[1])
    
    dp[(i, j)] = (min_recomputations + 1 if i == s else min_recomputations,
                   max_recomputations + 1 if i == s else max_recomputations)
    return dp[(i, j)]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
s, t = None, None
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

min_recomputations, max_recomputations = 0, float('inf')
for i in range(k-1):
    min_recomputations, max_recomputations = recompute_path(path[i], 0)
    s, t = path[i+1], path[i]

print(min_recomputations, max_recomputations)
