import sys

def solution():
    n = int(input())
    portals = list(map(int, input().split()))
    
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i].append(i-1)
        graph[i].append(portals[i-1])
    
    # Perform BFS to find the shortest path from room 1 to room (n+1)
    queue = [(1, 0)]  # (room, moves)
    visited = set()
    while queue:
        room, moves = queue.pop(0)
        if room == n+1:
            return moves
        for neighbor in graph[room]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, moves + 1))

print(solution() % 1000000007)
