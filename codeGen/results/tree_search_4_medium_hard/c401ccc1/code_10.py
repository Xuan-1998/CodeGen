def zookeeper(q):
    memo = {}
    for _ in range(q):
        u, v = map(int, input().split())
        if (u & v) == v:
            dp = [[False] * 30 for _ in range(30)]
            def dfs(i, j):
                if not dp[i][j]:
                    dp[i][j] = ((i >> j) & 1) or dfs((i // 2) | ((~i & (1 << j)) >> 1), j)
                return dp[i][j]
            print("YES" if dfs(u, v) else "NO")

zookeeper(int(input()))
