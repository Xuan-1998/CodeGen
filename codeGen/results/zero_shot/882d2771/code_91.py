def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i == 2:
            dp[i] = 1
        else:
            dp[i] = min(dp[i - 1], dp[i // 2] + i % 2) if i % 2 == 0 else min(dp[i - 1], dp[(i + 1) // 2] + 1)
    return dp[n]

t, l, r = map(int, input().split())
result = 0
for i in range(t):
    result += (t - i) * f(l + i)
result -= l * f(r)
print(result % (10**9 + 7))
