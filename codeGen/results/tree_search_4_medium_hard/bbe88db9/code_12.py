from collections import deque

def get_min_portal_moves(n):
    memo = {}
    queue = deque([(1, 0, False)])

    while queue:
        room, portals_used, ceiling_painted = queue.popleft()

        if room == n + 1:
            return portals_used % 1000000007

        if (room, portals_used, ceiling_painted) in memo:
            continue

        first_portal = [2 * i - 1 for i in range(1, room + 1)][0]
        second_portal = p[room - 1]

        if not ceiling_painted:
            queue.append((first_portal, portals_used + 1, True))
            queue.append((second_portal, portals_used + 1, False))

        else:
            queue.append((second_portal, portals_used + 1, ceiling_painted))

    return -1

n = int(input())
p = list(map(int, input().split()))
print(get_min_portal_moves(n))
