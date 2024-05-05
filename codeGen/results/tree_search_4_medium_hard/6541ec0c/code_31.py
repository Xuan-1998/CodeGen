import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[0]*(k+1) for _ in range(n+1)]

    def dfs(node, parent, mask):
        if node > 0:
            return False
        if node == n:
            return True

        for child in children[node]:
            if not dfs(child, node, (mask ^ values[child])):
                return False
        return True

    memo = {}

    def update_dp(node):
        for j in range(2, min(k+1, len(children)+1)):
            for child in children[node]:
                if child != node:
                    dp[node][j] = max(dp[node][j], dp[child][j-1])

    children = {}
    for edge in edges:
        u, v = edge
        if u not in children:
            children[u] = []
        if v not in children:
            children[v] = []
        children[u].append(v)
        children[v].append(u)

    update_dp(0)

    for j in range(k+1):
        dp[0][j] = 1 if dfs(n, -1, 0) else 0

    print("YES" if any(dp[-1][k]) else "NO")

solve()
