def solve(n):
    MOD = 998244353
    dp = {}

    def dfs(i, j):
        if i > j or j == 0:
            return 1
        if (i, j) in dp:
            return dp[(i, j)]
        res = 0
        for k in range(1, min(i+1, j+1)):
            res += dfs(k-1, j-1)
        res %= MOD
        dp[(i, j)] = res
        return res

    return dfs(n, n)

n = int(input())
print(solve(n))
