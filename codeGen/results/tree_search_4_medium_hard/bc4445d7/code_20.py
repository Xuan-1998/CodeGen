import sys

def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    prime_factors = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    parent = [-1] * (n + 1)

    def dfs(u):
        if parent[u] != -1:
            return
        parent[u] = u
        for v, w in edges:
            if v == u:
                dfs(w)
                parent[u] = min(parent[u], parent[v])
            elif w == u:
                dfs(v)
                parent[u] = min(parent[u], parent[w])

    for u in range(1, n + 1):
        dfs(u)

    for i in range(n - 1):
        u, v = edges[i]
        dp[u][v] = (dp[u][parent[u]] * dp[parent[u]][v]) % (10**9 + 7)
        if parent[u] == -1:
            dp[u][v] = min(dp[u][v], 1)

    total = 0
    for i in range(n - 1):
        u, v = edges[i]
        total += dp[u][v]

    print(total % (10**9 + 7))

if __name__ == "__main__":
    solve()
