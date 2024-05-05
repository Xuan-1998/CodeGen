def dfs(room, crosses):
    if room == n + 1:
        return 0
    if crosses % 2 != 0:
        portal = second_portals[room - 1]
    else:
        portal = first_portals[room - 1]
    crosses += 1
    return 1 + dfs(portal, crosses)

n = int(input())
first_portals = []
second_portals = []

for _ in range(n):
    p_i = int(input())
    if len(first_portals) == 0:
        first_portals.append(p_i)
    else:
        second_portals.append(p_i)

print(dfs(1, 0) % 1000000007)
