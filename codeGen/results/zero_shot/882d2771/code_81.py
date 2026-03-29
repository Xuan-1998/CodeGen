import sys

def f(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        if i % 2 == 1:
            dp[i] = min(dp[i-1], 1) + (i-1)//2
        else:
            dp[i] = dp[i//2]
    return dp[n]

def solve(t, l, r):
    res = 0
    for i in range(l, r+1):
        res += t * f(i)
    return str(res % (10**9 + 7))

t, l, r = map(int, input().split())
print(solve(t, l, r))
