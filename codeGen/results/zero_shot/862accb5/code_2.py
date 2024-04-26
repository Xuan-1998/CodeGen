import sys
from collections import defaultdict

def dfs(graph, node, parent, depth, low, visited, articulation_points, bridges):
    visited[node] = True
    depth[node] = low[node] = len(visited)
    children = 0
    
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            children += 1
            dfs(graph, neighbor, node, depth, low, visited, articulation_points, bridges)
            low[node] = min(low[node], low[neighbor])
            
            if low[neighbor] > depth[node]:
                bridges.append((node, neighbor, weight))
                
        elif neighbor != parent:
            low[node] = min(low[node], depth[neighbor])
            
    if parent is None and children > 1:
        articulation_points.add(node)
    elif parent is not None and low[node] >= depth[node]:
        articulation_points.add(node)

def find_bridges(n, roads):
    graph = defaultdict(list)
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    visited = [False] * (n + 1)
    depth = [0] * (n + 1)
    low = [0] * (n + 1)
    articulation_points = set()
    bridges = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, None, depth, low, visited, articulation_points, bridges)
    
    return bridges

def main():
    n = int(input())
    roads = [tuple(map(int, input().split())) for _ in range(n)]
    bridges = find_bridges(n, roads)
    
    # Calculate total inconvenience without each bridge
    total_inconvenience = sum(weight for _, _, weight in roads)
    min_inconvenience = total_inconvenience - max(weight for _, _, weight in bridges)
    
    print(min_inconvenience)

if __name__ == "__main__":
    main()
