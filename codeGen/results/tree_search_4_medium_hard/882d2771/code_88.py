def f(l, r):
    MOD = 10**9 + 7
    dp = [[0] * (r + 1) for _ in range(l + 1)]

    for k in range(1, l + 1):
        for i in range(k, r + 1):
            if i <= k:
                dp[k][i] = k
            else:
                dp[k][i] = min(dp[min(i - l, k)][min(i - l, k)] + (i - l), k)

    return sum(t * f(l, r) for t in range(t)) % MOD

t, l, r = map(int, input().split())
print(f(l, r))
