def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    prime_factors = list(map(int, input().split()))
    k = 1
    for p in prime_factors:
        k *= p

    dp = [[0] * (n+1) for _ in range(n+1)]

    def dfs(u, v):
        if u == v:
            return 0
        if dp[u][v] > 0:
            return dp[u][v]
        f = sum(edges[i][1] for i in range(len(edges)) if edges[i][0] == u and edges[i][1] != v)
        dp[u][v] = f + min(dfs(u-1, v-1), dfs(u-1, v), dfs(u, v-1))
        return dp[u][v]

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += dfs(i, j)
    print(ans % (10**9 + 7))

solve()
