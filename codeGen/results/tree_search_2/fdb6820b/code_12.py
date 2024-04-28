def count_ways(m, N, arr):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for x in arr:
        for i in range(N, x - 1, -1):
            dp[i] += dp[i - x]
            dp[i] %= MOD

    return dp[N]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(count_ways(m, N, arr))
