def f(l, r):
    MOD = 10**9 + 7
    dp = [[-1 for _ in range(r - l + 2)] for _ in range(t + 1)]

    def helper(k, n):
        if k == 0:
            return n - 1
        if n <= 1:
            return 0
        if dp[k][n] != -1:
            return dp[k][n]

        res = float('inf')
        for i in range(l, r + 1):
            res = min(res, helper(k - 1, i) + (k == t))
        dp[k][n] = res
        return res

    return sum(helper(i, l) for i in range(t)) % MOD

t, l, r = map(int, input().split())
print(f(l, r))
