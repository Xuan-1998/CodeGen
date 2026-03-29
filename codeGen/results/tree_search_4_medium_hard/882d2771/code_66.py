===BEGIN CODE===
def f(n):
    if n <= 2:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]

t, l, r = map(int, input().split())
print((t0 * f(l) + t1 * f(l + 1) + ... + tr * f(r) - l * f(r)) % (10**9 + 7))
===END CODE===
