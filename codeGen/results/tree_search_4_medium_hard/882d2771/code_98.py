def f(n):
    if n <= 1:
        return 0

    dp = {1: 0}

    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(i - 1, 1, -1):
            dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]

t, l, r = map(int, input().split())
print(f(r) % (10**9 + 7))
