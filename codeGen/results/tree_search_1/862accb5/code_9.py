import sys
from collections import defaultdict

def dfs(graph, start, visited):
    stack = [(start, 0)]
    farthest_node = start
    max_distance = 0
    while stack:
        node, distance = stack.pop()
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
        visited[node] = distance
        for neighbor, road_length in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, distance + road_length))
    return farthest_node, max_distance

def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    # Step 2a: First DFS to find one end of the longest path
    visited = {}
    farthest_node, _ = dfs(graph, 1, visited)

    # Step 2b: Second DFS to find the other end of the longest path and its length
    visited = {}
    _, max_inconvenience = dfs(graph, farthest_node, visited)

    # Output the result
    print(max_inconvenience)

if __name__ == "__main__":
    main()
