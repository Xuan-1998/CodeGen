import sys

def solve(n, portals):
    # Step 1: Calculate the number of rooms that are reachable from each room.
    reachable = [0] * (n + 2)
    for i in range(1, n + 1):
        reachable[i] += 1
        if i < portals[i - 1]:
            reachable[portals[i - 1]] += reachable[i]
        else:
            reachable[i] += reachable[portals[i - 1]]
    
    # Step 2: Find the shortest path from room 1 to room (n+1).
    queue = [(1, 0)]  # (room, moves)
    while queue:
        room, moves = queue.pop(0)
        if room == n + 1:
            return moves
        for neighbor in range(room + 1, n + 2):
            if reachable[neighbor] > 0:
                queue.append((neighbor, moves + 1))
    
    # If no path is found, return -1.
    return -1

n = int(sys.stdin.readline())
portals = [int(x) for x in sys.stdin.readline().split()]
print(solve(n, portals) % 1000000007)
