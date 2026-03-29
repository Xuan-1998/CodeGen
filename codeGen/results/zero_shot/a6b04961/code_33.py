import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start, end):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append((neighbor, dist + 1))
                visited[neighbor] = True
    return -1

def find_hedgehog():
    max_beauty = 0
    for start in range(1, n + 1):
        tail_dist = bfs(start, n)
        if tail_dist != -1:
            spines = [bfs(i, n) for i in range(start + 1, n + 1)]
            beauty = tail_dist * sum(spines)
            max_beauty = max(max_beauty, beauty)
    return max_beauty

print(find_hedgehog())
