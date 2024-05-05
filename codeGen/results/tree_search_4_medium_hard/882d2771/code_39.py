def beautycontest(t, l, r):
    MOD = 10**9 + 7

    # base case: f(1) = 0
    dp = {1: 0}

    for n in range(2, r+1):
        dp[n] = float('inf')
        for l1 in range(1, n//2 + 1):
            if l1 + (n - l1) == n:
                dp[n] = min(dp[n], dp[l1] + 1 + dp[n-l1])

    return sum(t[i] * (dp[li] - li for li in range(l, r+1)) % MOD
