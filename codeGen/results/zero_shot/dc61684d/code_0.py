from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def count_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, node, visited)
            components += 1
    return components

def remove_edge(graph, edge):
    u, v = edge
    graph[u].remove(v)
    graph[v].remove(u)

def add_edge(graph, edge):
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    edges = []
    
    # Building the graph
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    k = int(input())
    experiments = []
    
    for _ in range(k):
        li, ri = map(int, input().split())
        experiments.append((li, ri))
    
    for li, ri in experiments:
        # Remove the edge for the experiment
        remove_edge(graph, edges[li - 1])
        
        # Count the components
        print(count_components(graph, n))
        
        # Reconnect the edge
        add_edge(graph, edges[li - 1])

if __name__ == "__main__":
    main()
