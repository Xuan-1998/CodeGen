import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
    
    root = min((u for u in graph), key=lambda u: len(graph[u]))
    reversed_edges_count = 0
    
    for city in range(1, n+1):
        if city != root:
            visited = {city}
            queue = [(city, 1)]
            
            while queue:
                node, dist = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            
            reversed_edges_count = max(reversed_edges_count, len(visited) - 1)
    
    capitals = [root]
    min_reversed_edges_count = reversed_edges_count
    
    for _ in range(n-1):
        root = next((u for u in graph), None)
        reversed_edges_count = sum(len(graph[u]) for u in graph if u != root and len(graph[u]) > 0)
        
        if reversed_edges_count < min_reversed_edges_count:
            capitals = [root]
            min_reversed_edges_count = reversed_edges_count
        elif reversed_edges_count == min_reversed_edges_count:
            capitals.append(root)
    
    print(min_reversed_edges_count)
    print(*capitals, sep='\n')

if __name__ == "__main__":
    solve()
