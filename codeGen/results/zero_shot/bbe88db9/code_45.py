import sys

def dfs(room, crosses, portals):
    if room == n+1:
        return crosses % mod
    
    if (crosses % 2) == 0:
        return dfs(portals[room-1], crosses, portals)
    else:
        return dfs(room+1, crosses+1, portals)

n = int(input())
portals = list(map(int, input().split()))
mod = 10**9 + 7

print(dfs(1, 0, portals))
