import heapq
import sys

# Read the input graph represented as an adjacency list.
n, m, T = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u].append((v, t))

# Perform topological sorting on the given DAG.
def topological_sort(graph):
    visited = [False] * (n + 1)
    ordering = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited, ordering)
    
    return list(reversed(ordering))

def dfs(node, graph, visited, ordering):
    visited[node] = True
    for neighbor, _ in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, ordering)
    ordering.append(node)

# Define a function to perform Dijkstra's algorithm on the given graph.
def dijkstra(graph):
    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    
    pq = [(0, 1)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, t in graph[node]:
            new_d = d + t
            if new_d < dist[neighbor]:
                dist[neighbor] = new_d
                prev[neighbor] = node
                heapq.heappush(pq, (new_d, neighbor))
    
    return dist[n]

# Find the maximum number of vertices that can be visited within a time limit of T.
def solve(n, m, T):
    ordering = topological_sort(graph)
    
    cur_time = 0
    max_vertices = 0
    
    for node in ordering:
        edge_time = dijkstra({u: [(v, t)] for u, ((v, _),) in graph.items()})
        
        if cur_time + edge_time <= T:
            cur_time += edge_time
            max_vertices = len(ordering)
        else:
            break
    
    return max_vertices

print(solve(n, m, T))
