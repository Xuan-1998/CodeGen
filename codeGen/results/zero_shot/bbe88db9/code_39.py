import sys
from collections import deque

def min_portal_moves(n, p):
    G = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        G[i].append((i-1, 0))  # first portal
        G[i].append((p[i-1], 1))  # second portal

    queue = deque([(1, 0)])  # starting room and move count
    visited = set([1])
    moves = 0

    while queue:
        node, prev_move = queue.popleft()
        if node == n+1:
            return moves

        for neighbor, edge_type in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, (prev_move + (edge_type == 1)) % 2))
        moves += 1

    return -1  # should never reach here

n = int(input())
p = list(map(int, input().split()))
print(min_portal_moves(n, p) % 1000000007)
