def count_ways(N, m, arr):
    MOD = 10**9 + 7
    dp = {0: 1}  # base case: there's one way to form N=0

    def dfs(n):
        if n not in dp:
            for i in range(m):
                for j in range(i+1):
                    dp[n] = (dp.get(n, 0) + dp.get(n-arr[i], 0)) % MOD
        return dp[n]

    ans = 0
    for i in range(1, N+1):
        ans += dfs(i)
    return ans
