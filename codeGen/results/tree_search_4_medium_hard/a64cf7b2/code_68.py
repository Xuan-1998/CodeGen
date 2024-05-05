import sys

def max_vertices(t, path):
    if t < 0:  # Time limit exceeded
        return 0
    if (t, tuple(path)) in dp:
        return dp[(t, tuple(path))]
    
    vertices = len(set(path))  # Count unique vertices in the path
    
    if path[-1] == n:  # Reach vertex n
        return vertices
    
    max_visit = 0
    for edge in edges:
        u, v, t_edge = edge
        if v not in path and t_edge <= t:
            visit = max_vertices(t - t_edge, path + [v])
            max_visit = max(max_visit, visit)
    
    dp[(t, tuple(path))] = max_visit  # Store result in memoization dictionary
    
    return max_visit

n, m, T = map(int, input().split())
edges = [[*map(int, line.split())] for line in [input() for _ in range(m)]]

dp = {}

max_visit = max_vertices(T, [1])
print(max_visit)
path = []
t = T
while path[-1] != n:
    for edge in edges:
        u, v, t_edge = edge
        if v not in path and t_edge <= t:
            visit = dp.get((t - t_edge, tuple(path + [v])), 0)
            if visit > 0:
                path.append(v)
                break
    t -= t_edge

print(*path, sep='\n')
