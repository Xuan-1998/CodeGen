def f(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]

t, l, r = map(int, input().split())

expression = sum(ti * f(l + i) for i in range(r - l + 1)) - l * f(r)
print(expression % (10**9 + 7))
