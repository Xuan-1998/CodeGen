import sys

def dfs(node, parent, xor_value, visited):
    if node in visited:
        return

    visited.add(node)
    global current_xor
    current_xor ^= node_value[node]

    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node, current_xor, visited)

    if len(visited) > k:
        print("NO")
        sys.exit()

    if current_xor == 0:
        print("YES")
    else:
        print("NO")

n, k = map(int, input().split())
node_value = [int(x) for x in input().split()]
tree = {}
for _ in range(n-1):
    u, v = map(int, input().split())
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)
    tree[v].append(u)

node_value.sort()

current_xor = 0
for node in range(1, n):
    dfs(node, -1, current_xor, set())

