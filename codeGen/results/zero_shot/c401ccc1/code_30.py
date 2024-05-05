def dfs(u, v, visited):
    if u == v:
        return True
    if visited[u]:
        return False
    visited[u] = True
    for i in range(30):  # iterate through all bits
        if (u & (1 << i)) and ((v | (1 << i)) != v):
            return dfs(u & (1 << i), v | (1 << i), visited)
    return False

def infinite_zoo(q):
    for _ in range(q):
        u, v = map(int, input().split())
        visited = [False] * (2**30)  # initialize bitvector
        print("YES" if dfs(u, v, visited) else "NO")
