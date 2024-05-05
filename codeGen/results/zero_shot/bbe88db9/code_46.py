from collections import deque

n = int(input())
graph = {}
for i in range(n+1):
    p_i = int(input()) - 1
    if i not in graph:
        graph[i] = []
    if p_i not in graph:
        graph[p_i] = []
    graph[i].append((p_i, 0))  # 0 represents the first portal

def bfs(graph, start):
    queue = deque([(start, 0)])  # (room, number of moves)
    visited = set()
    while queue:
        room, moves = queue.popleft()
        if room == n:
            return moves
        for neighbor in graph[room]:
            if neighbor[1] == 1:  # second portal
                next_moves = moves + 1
            else:  # first portal
                next_moves = moves
            next_room = neighbor[0]
            if next_room not in visited:
                queue.append((next_room, next_moves))
                visited.add(next_room)

print(bfs(graph, 0) % (10**9 + 7))
