def f(n):
    if n == 2:
        return 1  # Base case: one comparison for two participants

    if dp[n] != -1:
        return dp[n]

    if n % 2 == 0:
        dp[n] = f(n // 2) + n
    else:
        dp[n] = f((n - 1) // 2) + 1

    return dp[n]


t, l, r = map(int, input().split())
dp = [-1] * (r + 1)
ans = ((t * f(r)) % (10**9 + 7)) - (l * f(l))
print(ans)
