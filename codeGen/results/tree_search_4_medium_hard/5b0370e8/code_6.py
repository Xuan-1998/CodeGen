def count(k, n):
    dp = {}
    def dfs(k, n):
        if k < 0:
            return dp.get((k, n), 0)
        if (k, n) in dp:
            return dp[(k, n)]
        res = 0
        for i in range(2**k):
            and_val = i & ((1 << k) - 1)
            xor_val = i ^ ((1 << k) - 1)
            if and_val >= xor_val:
                res += dfs(k-1, n-1)
        dp[(k, n)] = (res % (10**9+7))
        return dp[(k, n)]
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(dfs(k, n))

