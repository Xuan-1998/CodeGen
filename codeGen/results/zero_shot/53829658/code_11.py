import sys

def find_min_reversals(n, roads):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n+1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)  # Since it's a tree, we only need to add edges once

    def dfs(v):
        visited = [False] * (n + 1)
        depth = [0] * (n + 1)
        max_distance = 0
        for u in range(1, n+1):
            if not visited[u]:
                d = dfs_util(u, v, visited, depth)
                max_distance = max(max_distance, d)
        return max_distance

    def dfs_util(v, parent, visited, depth):
        nonlocal max_distance
        visited[v] = True
        for u in graph[v]:
            if u != parent:
                if not visited[u]:
                    depth[u] = depth[v] + 1
                    d = dfs_util(u, v, visited, depth)
                    max_distance = max(max_distance, d)
                else:
                    depth[u] = depth[v]
        return depth[v]

    min_reversals = 0
    capital_cities = []
    for i in range(1, n+1):
        if dfs(i) > min_reversals:
            min_reversals = dfs(i)
            capital_cities = [i]
        elif dfs(i) == min_reversals:
            capital_cities.append(i)

    print(min_reversals)
    print(*capital_cities, sep='\n')

# Read input
n = int(input())
roads = []
for _ in range(n-1):
    u, v = map(int, input().split())
    roads.append((u, v))

find_min_reversals(n, roads)
