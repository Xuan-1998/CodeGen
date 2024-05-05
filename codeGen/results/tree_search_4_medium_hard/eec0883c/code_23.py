import sys
from collections import deque

def read_input():
    n = int(sys.stdin.readline())
    w = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n+2)]
    
    for i in range(1, n):
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u].append((v, c))
        graph[v].append((u, 0))  # Reverse edge with zero capacity
    
    return n, w, graph

def bfs(graph, source, sink, parent):
    visited = [False] * (len(graph) + 1)
    queue = deque()
    
    queue.append(source)
    visited[source] = True
    
    while queue:
        node = queue.popleft()
        
        for neighbor, capacity in graph[node]:
            if not visited[neighbor] and capacity > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node
                
                if neighbor == sink:
                    return True
    
    return False

def dfs(graph, source, sink, parent, flow):
    if source == sink:
        return flow
    
    for neighbor, capacity in graph[source]:
        if capacity > 0 and not visited[neighbor]:
            visited[neighbor] = True
            new_flow = min(flow, capacity)
            
            if (new_flow := dfs(graph, neighbor, sink, parent, new_flow)) > 0:
                graph[parent[neighbor]][neighbor] -= new_flow
                return new_flow
            
    return 0

def edmonds_karp(graph, source, sink):
    parent = [-1] * (len(graph) + 1)
    
    while bfs(graph, source, sink, parent):
        flow = float('inf')
        
        for node in range(len(graph)):
            if node == sink:
                break
            
            visited[node] = False
        
        for node in range(len(graph)):
            if node == sink or not visited[node]:
                flow = min(flow, dfs(graph, node, sink, parent, flow))
                
        print(f"Flow: {flow}")

n, w, graph = read_input()
visited = [False] * (len(graph) + 1)
edmonds_karp(graph, 0, n+1)
