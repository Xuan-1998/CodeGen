import heapq

def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    prime_factors = list(map(int, input().split()))

    dp = {(): 1}

    def dfs(node, parent):
        if (node,) in dp:
            return dp[(node,)]

        if parent == -1:
            parent = node

        res = float('inf')
        for child in edges:
            if child[0] == node and child != (parent, node):
                res = min(res, dfs(child[0], node) * dfs(child[1], node))
            elif child[1] == node and child != (node, parent):
                res = min(res, dfs(child[0], node) * dfs(parent, child[1]))

        dp[(node,)] = res
        return res

    res = 0
    for edge in edges:
        u, v = edge
        res += (dfs(u, -1) + dfs(v, u)) % (10**9 + 7)

    print(res)

solve()
