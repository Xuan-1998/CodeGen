import sys

def read_input():
    n, m, T = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))
    return n, m, T, edges

def preprocess_graph(n, m, T, edges):
    # Create a dictionary to store the graph
    graph = {i: [] for i in range(1, n+1)}
    for u, v, t in edges:
        graph[u].append((v, t))
    return graph

def find_longest_path(n, T, graph):
    # Initialize dp array and visited set
    dp = [0] * (n + 1)
    visited = set()
    
    def dfs(v, time_left):
        if v == n:
            return time_left
        if v in visited:
            return 0
        
        visited.add(v)
        
        max_time = 0
        for neighbor, t in graph[v]:
            max_time = max(max_time, dfs(neighbor, time_left - t))
        dp[v] = max_time + 1
        return dp[v]
    
    return max(dfs(i, T) for i in range(1, n+1))

n, m, T, edges = read_input()
graph = preprocess_graph(n, m, T, edges)
k = find_longest_path(n, T, graph)

print(k)
visited_vertices = [i for i in range(1, n+1) if dp[i] == k]
print(*visited_vertices, sep=' ')
