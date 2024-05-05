def f(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if i % (j + 1) == 0:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]

t, l, r = map(int, input().split())
print((t * f(l) + sum(ti * f(li) for ti, li in zip(map(int, input().split()), range(l + 1, r + 1))) - l * f(r)) % (10**9 + 7))
