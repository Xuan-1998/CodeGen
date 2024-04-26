import sys
from collections import defaultdict

def dfs(node, parent, graph, subtree_sizes, depths):
    subtree_sizes[node] = 1
    max_depth = 0
    for neighbor, length in graph[node]:
        if neighbor != parent:
            depth = dfs(neighbor, node, graph, subtree_sizes, depths) + length
            subtree_sizes[node] += subtree_sizes[neighbor]
            if depth > max_depth:
                max_depth = depth
    depths[node] = max_depth
    return max_depth

def find_min_inconvenience(n, roads):
    graph = defaultdict(list)
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))

    subtree_sizes = [0] * (n + 1)
    depths = [0] * (n + 1)
    
    # Run DFS to calculate subtree sizes and depths
    dfs(1, -1, graph, subtree_sizes, depths)

    # Find the edge to remove from the longest path
    min_inconvenience = float('inf')
    for u, v, l in roads:
        inconvenience = subtree_sizes[u] * subtree_sizes[v] * l
        min_inconvenience = min(min_inconvenience, inconvenience)

    return min_inconvenience

def main():
    n = int(sys.stdin.readline().strip())
    roads = []
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        roads.append((u, v, l))
    print(find_min_inconvenience(n, roads))

if __name__ == "__main__":
    main()
