import sys

def f(n):
    if n == 2:
        return 3
    dp = [0] * (n + 1)
    dp[1], dp[2] = 2, 3
    for i in range(3, n + 1):
        dp[i] = min(dp[i-1] + i - 1, dp[i-2] + i - 2)
    return dp[n]

t, l, r = map(int, input().split())
result = 0
for i in range(l, r+1):
    result += t * f(i) % (10**9 + 7)
print(result % (10**9 + 7))
