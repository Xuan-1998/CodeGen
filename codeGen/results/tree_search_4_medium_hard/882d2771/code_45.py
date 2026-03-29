def beautyShops(t, l, r):
    MOD = 10**9 + 7
    dp = [float('inf')] * (r - l + 1)
    dp[0] = 0

    for i in range(l, r + 1):
        for k in range(i):
            if k >= l:
                dp[i - k - 1] = min(dp[i - k - 1], dp[k] + k)
        dp[i] = dp[i - 1] + i
    return (dp[r] * t[0] + dp[r-1] * t[1] + ... + dp[l] * t[r]) % MOD

t, l, r = map(int, input().split())
print(beautyShops(t, l, r))
