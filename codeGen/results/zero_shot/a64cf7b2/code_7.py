import heapq
from collections import defaultdict

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    visited = set()
    max_time = 0
    queue = [(T, 1)]

    while queue:
        time, vertex = heapq.heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, edge_time in graph[vertex]:
                new_time = time - edge_time
                if new_time > max_time and neighbor == n:
                    max_time = new_time
                    break
                elif new_time <= T:
                    heapq.heappush(queue, (new_time, neighbor))

    print(max_time)
    visited = list(visited)
    for i in range(len(visited) - 1):
        print(visited[i], end=' ')
    print(visited[-1])
