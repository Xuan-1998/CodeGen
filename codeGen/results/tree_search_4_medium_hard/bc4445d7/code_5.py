def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    primes = list(map(int, input().split()))

    MOD = 10**9 + 7
    INF = float('inf')
    
    dp = [[INF] * (n+1) for _ in range(n+1)]

    def dfs(u):
        if u == n:
            return 0
        
        if dp[u][n] != INF:
            return dp[u][n]

        res = INF
        for v in edges:
            if v[0] == u:
                res = min(res, dfs(v[1]) + f(u, v[1]))
            elif v[1] == u:
                res = min(res, dfs(v[0]) + f(u, v[0]))

        dp[u][n] = res
        return res

    def f(i, j):
        # calculate the sum of integers on path from node i to j
        pass  # implement this part

    print(dfs(1) % MOD)

