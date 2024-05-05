from collections import defaultdict

def find_max_beauty(n, m, edges):
    # build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    max_beauty = 0
    visited = set()

    def dfs(u, path_length=1):
        nonlocal max_beauty
        if u not in visited:
            visited.add(u)
            max_beauty = max(max_beauty, path_length * (len(visited) - 1))
            for v in graph[u]:
                if v not in visited:
                    dfs(v, path_length + 1)

    # start DFS from each unvisited node
    for i in range(n):
        if i not in visited:
            dfs(i)

    return max_beauty

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

print(find_max_beauty(n, m, edges))
