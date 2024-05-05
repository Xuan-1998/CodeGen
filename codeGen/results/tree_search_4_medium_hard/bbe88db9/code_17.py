=BEGIN CODE=
import sys

def dfs(room, visited):
    if (room, visited) in dp:
        return dp[(room, visited)]
    
    next_room = room + 1
    if room < n+1 and visited == 0:
        next_room = portal_map[room]
    
    res = 1 + dfs(next_room, not visited) if crosses % 2 != 0 else dfs(next_room, visited)
    dp[(room, visited)] = res
    return res

n, p_map = map(int, input().split())
p_map = {i: j for i, j in zip(range(1, n+1), [0] + list(map(int, input().split())))}
crosses = 0
dp = {}

print(dfs(1, 0)) % (10**9 + 7)
=END CODE=
