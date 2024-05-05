import sys
from collections import deque, defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    max_tail_length = 0
    max_spines = 0

    for node in range(1, n+1):
        queue = deque([(node, [node])])
        tail_length = 0
        while queue:
            current_node, path = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                next_nodes = graph[current_node]
                for neighbor in next_nodes:
                    if neighbor not in visited and neighbor != node:
                        queue.append((neighbor, path + [neighbor]))
                        tail_length += 1
        max_tail_length = max(max_tail_length, tail_length)

    for _ in range(100):  # This is a rough estimate, we can improve later
        max_spines += m

    return max_tail_length * max_spines

print(solve())
