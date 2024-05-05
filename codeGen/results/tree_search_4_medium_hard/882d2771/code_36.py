def beautycontest():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7

    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        dp[i] = float('inf')
        for j in range(1, (i + 1) // 2 + 1):
            if i >= 2j:
                dp[i] = min(dp[i], dp[j - 1] + 1 + dp[i - 2 * j])

    result = t * dp[l]
    for i in range(l + 1, r + 1):
        result = (result + t * dp[i]) % MOD
    print(result)

beautycontest()
