from sys import stdin

def dfs(u, visited):
    if u in visited:
        return False
    visited.add(u)
    for w in range(2**30):
        if (u & w) == w and w not in visited:
            if dfs(w, visited):
                return True
    return False

q = int(stdin.readline())
for _ in range(q):
    u, v = map(int, stdin.readline().split())
    if dfs(u, set()):
        print("YES")
    else:
        print("NO")
