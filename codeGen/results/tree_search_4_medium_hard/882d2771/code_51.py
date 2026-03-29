def f(n):
    if n < 2:
        return 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 2:
            dp[i] = 0
        else:
            dp[i] = min(dp[i - 1], dp[i // 2]) + 1
    return dp[n]

t, l, r = map(int, input().split())
print((t * f(l)) % (10**9 + 7) + sum(ti * (f(li) - li) for ti, li in zip(map(int, str(r-l+1)), range(l, r+1))) % (10**9 + 7))
