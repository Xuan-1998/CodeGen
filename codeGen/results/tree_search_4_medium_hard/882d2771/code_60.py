def solve(t, l, r):
    mod = 10**9 + 7
    dp = [0] * (r + 1)
    for i in range(2, r + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2] + i // 2
        else:
            dp[i] = min(dp[(i - 1) // 2] + (i - 1) // 2 + 1, dp[i // 2] + i // 2)
    res = sum(t * (dp[l - 1] - l) for t in range(1, t + 1))
    return str(int(res % mod))

t, l, r = map(int, input().split())
print(solve(t, l, r))
