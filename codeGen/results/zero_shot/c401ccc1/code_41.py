def dfs(u, v):
    if u & v == v:  # base case: if u&v=v, then v is reachable from u
        return True
    for i in range(30):  # iterate through all possible edges
        w = u | (1 << i)  # generate a new vertex w that satisfies the condition w&u=u
        if dfs(w, v):  # recursively explore from w to v
            return True
    return False

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if dfs(u, v) else "NO")
