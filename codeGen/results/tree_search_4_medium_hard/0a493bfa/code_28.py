import sys
from math import gcd

# Read input from stdin
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        if a[i - 1] % b[j - 1] == 0:
            dp[i][j] = max(dp[i - 1][j], f(a[i - 1], dp[i - 1]))
        else:
            dp[i][j] = max(dp[i - 1][j - 1], f(a[i - 1], dp[i - 1]))

print(max(dp[n]))

def f(x, dp):
    g = x
    for y in range(1, x + 1):
        if gcd(y, x) != 1:
            g -= y
    return max(dp[x // y] for y in range(1, int(x ** 0.5) + 1))

