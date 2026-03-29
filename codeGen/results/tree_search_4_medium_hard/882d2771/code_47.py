def beautycontest():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7

    dp = [0] * (r // 2 + 1)
    for i in range(1, r // 2 + 1):
        if i == 1:
            dp[i] = 1
        else:
            dp[i] = 1 + min(dp[j] for j in range(i))

    ans = sum(t * (r - l) ** i // (i + 1) * dp[i] for i in range(r // 2, -1, -1))
    print(ans % MOD)
