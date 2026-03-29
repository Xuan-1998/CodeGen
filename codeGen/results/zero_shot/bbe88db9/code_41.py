import sys
from collections import deque

def solve(n, portals):
    queue = deque([(1, 0)])  # (room, steps)
    visited = set()
    while queue:
        room, steps = queue.popleft()
        if room == n + 1:  # target room reached
            return steps % 1000000007
        if room not in visited:
            visited.add(room)
            for next_room in [room - 1, portals[room - 2]]:
                if 1 <= next_room <= n + 1 and next_room not in visited:
                    queue.append((next_room, steps + 1))

n = int(sys.stdin.readline())
portals = [int(x) for x in sys.stdin.readline().split()]
print(solve(n, portals))
