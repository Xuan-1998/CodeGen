import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, graph

def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == end:
                    return path + [neighbor]
                elif neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

def solve():
    n, graph = read_input()
    max_beauty = 0
    for start_vertex in range(1, n):
        for end_vertex in range(start_vertex+1, n):
            path = bfs(graph, start_vertex, end_vertex)
            if path:
                beauty = len(path) * (n - len(path))
                max_beauty = max(max_beauty, beauty)
    print(max_beauty)

if __name__ == "__main__":
    solve()
