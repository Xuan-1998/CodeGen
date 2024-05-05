import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    capital = 0
    min_distance = float('inf')
    for i in range(1, n+1):
        distance = bfs(i)
        if distance < min_distance:
            min_distance = distance
            capital = i

    print(min_distance)
    print(cities_to_capital_order())

def bfs(start):
    visited = [False] * (n+1)
    queue = deque([(start, 0)])  # (city, distance)
    while queue:
        city, dist = queue.popleft()
        if not visited[city]:
            visited[city] = True
            for neighbor in graph[city]:
                queue.append((neighbor, dist + 1))
    return [i for i in range(1, n+1) if not visited[i]].index(start)

def cities_to_capital_order():
    order = []
    for i in range(n+1):
        if i != capital:
            order.append(i)
    return str(order).replace(" ", "")

solve()
