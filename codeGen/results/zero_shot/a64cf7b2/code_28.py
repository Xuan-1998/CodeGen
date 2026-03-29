from collections import defaultdict

def find_longest_path():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    visited = set()
    longest_path = []
    
    def dfs(vertex, time_left, path):
        nonlocal longest_path
        if len(path) > len(longest_path):
            longest_path = list(path)
        if vertex == n:
            return
        if vertex in visited:
            return
        visited.add(vertex)
        
        for neighbor, edge_time in graph[vertex]:
            new_time_left = time_left - edge_time
            if new_time_left >= 0 and len(path) + 1 > len(longest_path):
                dfs(neighbor, new_time_left, path + [vertex])
        
        visited.remove(vertex)

    dfs(1, T, [])
    
    print(len(longest_path))
    print(' '.join(map(str, longest_path)))

find_longest_path()
