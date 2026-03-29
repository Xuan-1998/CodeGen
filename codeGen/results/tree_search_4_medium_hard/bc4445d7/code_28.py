import sys
input = sys.stdin.readline

def read():
    return [int(x) for x in input().split()]

def solve():
    n, m, k = read()
    p = read()
    dp = [[0] * (n+1) for _ in range(n+1)]
    edges = []
    for i in range(n-1):
        u, v = read()
        edges.append((u, v))

    def dfs(u, v):
        if dp[u][v] > 0:
            return
        dp[u][v] = min([f(x,y) for (x, y) in edges if x < u and y > v])
        if u == v:
            dp[u][v] = f(u,u)
        else:
            for k in range(u+1, v):
                dfs(u, k-1)
                dfs(k+1, v)
                dp[u][v] = max(dp[u][v], dp[u][k-1] * dp[k+1][v])

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):
            dfs(i, j)

    return sum([dp[i][j] for i in range(1, n) for j in range(i+1, n)]) % (10**9 + 7)

print(solve())
