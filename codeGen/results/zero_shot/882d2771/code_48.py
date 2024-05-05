import sys

def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2] + 1
        else:
            dp[i] = dp[(i - 1) // 2] + 1
    return dp[n]

t, l, r = map(int, input().split())
res = sum(t * f(i) for i in range(l, r + 1)) - l * f(r)
print(res % (10**9 + 7))
