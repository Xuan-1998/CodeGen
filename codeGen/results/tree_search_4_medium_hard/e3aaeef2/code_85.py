def solve():
    t = int(input())
    mod = 10**9 + 7

    dp = {}
    def dfs(n, m):
        if (n, m) not in dp:
            if n == 0:
                dp[(n, m)] = 0
            elif m == 0:
                dp[(n, m)] = len(str(n))
            else:
                dp[(n, m)] = 1 + sum(dfs(k, m-1) for k in range(10)) % mod
        return dp[(n, m)]

    for _ in range(t):
        n, m = map(int, input().split())
        print(dfs(n, m) % mod)

solve()
