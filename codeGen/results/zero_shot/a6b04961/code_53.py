import sys

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Find all connected components (connected subgraphs)
visited = [False] * n
components = []
for i in range(n):
    if not visited[i]:
        component = []
        dfs(i, visited, edges, component)
        components.append(component)

max_beauty = 0
for component in components:
    # Find the longest simple path (tail) for each connected component
    tail_length = len(dfs_longest_path(component))
    
    # Count the number of spines for each connected component
    spine_count = 0
    for edge in edges:
        if any(node not in component for node in edge):
            spine_count += 1
    
    # Calculate the beauty of this connected component
    beauty = tail_length * spine_count
    max_beauty = max(max_beauty, beauty)

print(max_beauty)

def dfs_longest_path(component):
    visited = [False] * n
    longest_path = []
    for node in component:
        if not visited[node]:
            path = []
            dfs(node, visited, edges, path)
            longest_path.append(path)
    return max(longest_path, key=len)

def dfs(node, visited, edges, path):
    visited[node] = True
    path.append(node)
    for edge in edges:
        if edge[0] == node and edge[1] not in path:
            dfs(edge[1], visited, edges, path)
        elif edge[1] == node and edge[0] not in path:
            dfs(edge[0], visited, edges, path)
