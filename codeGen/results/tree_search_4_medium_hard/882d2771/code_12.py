import sys
input = sys.stdin.readline

t, l, r = map(int, input().split())

def grp(n):
    if n == 1:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i // 2, i + 1):
            dp[i] = min(dp[i], 1 + dp[j])
    return dp[n]

def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + grp(n // 2)
    else:
        return t * grp(n // t)

print((f(r) - l * f(l)) % (10**9 + 7))
