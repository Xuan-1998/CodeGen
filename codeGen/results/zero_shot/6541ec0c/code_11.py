import sys

def dfs(u, parent, xor_val):
    global visited, component_xor
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs(v, u, xor_val ^ node_values[v])
        elif v != parent:
            return False
    return True

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    node_values = [int(x) for x in sys.stdin.readline().split()]
    adj_list = [[] for _ in range(n)]
    visited = [False] * n
    component_xor = {}
    for i in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    if not any(not dfs(i, -1, node_values[i]) for i in range(n)):
        print("NO")
    else:
        print("YES" if all(xor_val == list(component_xor.values())[0] for xor_val in component_xor.values()) else "NO")

