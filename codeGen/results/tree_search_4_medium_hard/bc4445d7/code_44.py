import sys

T = int(input())
memoization = {}
for _ in range(T):
    n = int(input())
    tree = {}
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)

    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p

    total_distribution_index = 0
    for node in tree:
        code = 1
        for child in tree[node]:
            code *= dfs(node, child)
        total_distribution_index += code % (10**9 + 7)

    print(total_distribution_index % (10**9 + 7))

def dfs(u, v):
    global code
    if (u, v) in memoization:
        return memoization[(u, v)]
    code = 1
    for child in tree[v]:
        code *= dfs(v, child)
    memoization[(u, v)] = code % (10**9 + 7)
    return code % (10**9 + 7)
