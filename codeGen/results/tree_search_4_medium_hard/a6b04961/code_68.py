import sys

def take_current_state(state, edges):
    if not edges:
        return 0

    max_beauty = 0
    for edge in edges:
        u, v = edge
        if u == state[1] or v == state[1]:
            new_state = (state[0] + 1, v)
            beauty = take_current_state(new_state, [edge])
            max_beauty = max(max_beauty, state[0] * len(edges) + beauty)

    return max_beauty

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u - 1, v - 1))

print(take_current_state((0, -1), edges))
