def find_max_beauty():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = {i: set() for i in range(n)}
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Find the longest simple path (the tail) using DFS
    visited = [False] * n
    max_length = 0
    for start in range(n):
        if not visited[start]:
            length, _ = dfs(graph, start, None, visited)
            max_length = max(max_length, length)
    
    # Count the number of spines
    spine_count = 0
    for u, v in edges:
        if (u in visited and v not in visited) or (v in visited and u not in visited):
            spine_count += 1
    
    return max_length * spine_count

def dfs(graph, start, parent, visited):
    visited[start] = True
    length = 1
    for neighbor in graph[start]:
        if neighbor != parent:
            if not visited[neighbor]:
                length += dfs(graph, neighbor, start, visited)[0]
            else:
                length += 1
    return length, start

print(find_max_beauty())
