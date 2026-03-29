import sys

def dfs(node, parent, k, memo):
    if (node, parent) in memo:
        return memo[(node, parent)]

    if parent == -1:  # leaf node
        memo[(node, parent)] = True
        return True

    xor_value = 0
    for child in children[node]:
        if child != parent:
            xor_value ^= dfs(child, node, k, memo)

    if xor_value == 0:
        memo[(node, parent)] = False
        return False

    if all(dfs(child, node, k - 1, memo) and xor_value ^ (child in children[node]) for child in children[node]):
        memo[(node, parent)] = True
        return True

    memo[(node, parent)] = False
    return False

n, k = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))
children = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    children[u].append(v)
    children[v].append(u)

print('YES' if dfs(0, -1, k, {}) else 'NO')
