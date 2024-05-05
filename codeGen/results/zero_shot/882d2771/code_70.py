def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + i, dp[i // 2] + i if i % 2 == 0 else dp[i - 1] + i)

    return dp[n]

t, l, r = map(int, input().split())
t_sum = sum(t * f(i) for i in range(l, r + 1))
result = t_sum - l * f(r)
print(result % (10 ** 9 + 7))
