import sys
n = int(sys.stdin.readline().strip())
p_rooms = list(map(int, sys.stdin.readline().strip().split()))
visited = {i: 0 for i in range(1, n+2)}

def dfs(room):
    if room == (n+1):
        return 1
    if visited[room] % 2 == 0:
        return dfs(p_rooms[room-1]) + 1
    else:
        return dfs(room-1) + 1

print(dfs(1)) % (10**9 + 7)
