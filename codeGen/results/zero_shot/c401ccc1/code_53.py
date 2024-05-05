import sys

def and_edge(u, v):
    return u & v == v

def dfs(u, v, visited):
    if u == v:
        return True
    for i in range(30):
        mask = (1 << i)
        if not visited.get(mask, False) and and_edge(u, u | mask):
            visited[mask] = True
            if dfs(u | mask, v, visited):
                return True
    return False

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    visited = {}
    print("YES" if dfs(u, v, visited) else "NO")
