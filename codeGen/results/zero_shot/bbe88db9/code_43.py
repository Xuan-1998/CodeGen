from collections import deque

def bfs():
    queue = deque([(1, 0)])  # initialize with room 1, 0 crosses
    visited = set()
    while queue:
        state = queue.popleft()
        room, crosses = state
        if room == n + 1:  # reached the goal room (n+1)
            return crosses
        if room not in visited:
            visited.add(room)
            for next_state in [transition(state)]:
                queue.append(next_state)
    return -1  # unreachable

n = int(input())  # read input
p = list(map(int, input().split()))  # read p[i] values
print(bfs() % (10**9 + 7))  # print result modulo 10000
