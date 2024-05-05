def dfs(node, parent, xor):
    node_value = values[node - 1]
    new_xor = xor ^ node_value
    for child in adj_list[node]:
        if child != parent:
            dfs(child, node, new_xor)

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    adj_list = [[] for _ in range(n)]
    for i in range(1, n):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    result = []
    for node in range(n):
        parent = -1
        xor = 0
        dfs(node, parent, xor)

    return True

for i, (n, k) in enumerate(zip(input().split(), input().split())):
    if solve():
        print("YES")
    else:
        print("NO")
