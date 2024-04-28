def count_ways(arr, N):
    mod = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in arr:
            if i - num >= 0:
                dp[i] += dp[i - num]
                dp[i] %= mod

    return dp[N]
