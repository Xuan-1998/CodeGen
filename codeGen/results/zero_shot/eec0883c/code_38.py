import sys

def solve():
    n = int(sys.stdin.readline().strip())
    w = list(map(int, sys.stdin.readsplitlines(n)))

    tree = [[] for _ in range(n)]
    for i in range(n-1):
        u, v, c = map(int, sys.stdin.readline().strip().split())
        tree[u].append((v, c))
        tree[v].append((u, c))

    def dfs(node, parent, gas):
        max_gas = 0
        for child, cost in tree[node]:
            if child != parent:
                new_gas = min(gas, w[child] - cost)
                max_gas = max(max_gas, dfs(child, node, new_gas) + new_gas)
        return max_gas

    print(dfs(0, -1, w[0]))

solve()
