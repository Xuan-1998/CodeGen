def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = list(map(int, input().split()))
        m = int(input())
        prime_factors = list(map(int, input().split()))

        dp = [[0] * (m + 1) for _ in range(n)]
        memo = {}

        def f(u, v):
            if u > v:
                return f(v, u)
            if (u, v) not in memo:
                memo[(u, v)] = sum(1 / p for p in prime_factors[:v - u]) + edges[v - 1]
            return memo[(u, v)]

        for i in range(n):
            for j in range(m):
                dp[i][j] = max(dp[k][min(j, m - 1)] + f(i, k) for k in range(i))

        print((dp[0][m - 1] + sum(f(1, u) for u in range(2, n))) % (10**9 + 7))

solve()
