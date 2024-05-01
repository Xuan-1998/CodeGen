import sys

def f(i, visited):
    if i == t:
        return 0, 0
    
    # If the driver chooses to follow the recommended path
    min_recomputations = sys.maxsize
    max_recomputations = -sys.maxsize
    for neighbor in graph[i]:
        if neighbor not in visited:
            min_path, max_path = f(neighbor, visited | {i})
            min_recomputations = min(min_recomputations, 1 + min_path)
            max_recomputations = max(max_recomputations, 1 + max_path)
    
    # If the driver chooses to recompute the shortest path
    min_path = sys.maxsize
    max_path = -sys.maxsize
    for neighbor in graph[i]:
        if neighbor not in visited:
            min_path, max_path = f(neighbor, visited | {i})
            min_recomputations = min(min_recomputations, 1 + min_path)
            max_recomputations = max(max_recomputations, 1 + max_path)
    
    return min_recomputations, max_recomputations

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

k = int(input())
path = list(map(int, input().split()))

min_recomputations = min_recomputations = 0
max_recomputations = max_recomputations = 0

visited = set()
for i in path:
    visited.add(i)
    min_recomputation, max_recomputation = f(i - 1, visited)
    min_recomputations += min_recomputation
    max_recomputations += max_recomputation
    
print(min_recomputations, max_recomputations)
