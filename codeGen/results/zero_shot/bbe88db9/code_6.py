import sys

n = int(input())
p = list(map(int, input().split()))

crosses = 0
def dfs(room):
    global crosses
    if room == n + 1:
        return 0
    
    next_room = (room * 2) % (n + 1)
    
    if p[room - 1] != next_room and (crosses & 1):
        next_room = p[room - 1]
    
    crosses ^= 1
    return 1 + dfs(next_room)

print(dfs(1))
