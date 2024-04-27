from collections import defaultdict

# Reads input and returns the graph and the experiments
def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(set)
    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)
        edges.append((x, y))
    k = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(k)]
    return n, graph, edges, experiments

# DFS to find connected components
def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

# Counts the number of connected components
def count_components(n, graph):
    visited = [False] * (n + 1)
    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node, graph, visited)
            components += 1
    return components

def main():
    n, graph, edges, experiments = read_input()
    
    for li, ri in experiments:
        # Remove the edge for the experiment
        graph[edges[li - 1][0]].remove(edges[li - 1][1])
        graph[edges[li - 1][1]].remove(edges[li - 1][0])
        
        # Count and output the number of connected components
        print(count_components(n, graph))
        
        # Reconnect the edge after the experiment
        graph[edges[li - 1][0]].add(edges[li - 1][1])
        graph[edges[li - 1][1]].add(edges[li - 1][0])

if __name__ == '__main__':
    main()
