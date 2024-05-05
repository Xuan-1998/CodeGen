import sys

def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1]) + 1
        else:
            dp[i] = min(dp[(i - 1) // 2], dp[(i + 1) // 2]) + 1 if i % 4 != 3 else dp[i - 1] + 1
    return dp[n]

t, l, r = map(int, input().split())
print((sum(range(1, t + 1)) * f(l)) % (10**9 + 7) - (l * f(r)) % (10**9 + 7))
