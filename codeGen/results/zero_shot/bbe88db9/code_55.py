import sys
from collections import deque

def solve(n, portals):
    # Create a graph represented as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i % 2:
            graph[i].append((i - 1, 0))  # First portal leads to room (i-1)
            graph[i].append((portals[i - 1], 1))  # Second portal leads to room p_i
        else:
            graph[i].append((portals[i - 1], 0))  # First portal leads to room p_i
            graph[i].append((i + 1, 1))  # Second portal leads to room (i+1)

    # Perform BFS from the starting room (room 1)
    queue = deque([(1, 0)])  # Initialize the queue with the starting room and no moves
    visited = set([1])  # Keep track of visited rooms

    while queue:
        room, moves = queue.popleft()
        if room == n + 1:  # If we reached the goal room, return the number of moves
            return moves % (10**9 + 7)

        for neighbor, portal_used in graph[room]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, moves + (portal_used == 1)))

    # If we couldn't reach the goal room, it means the maze is impossible to escape
    return -1

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    portals = list(map(int, sys.stdin.readline().split()))
    result = solve(n, portals)
    print(result)
