import sys

def f(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + f(n // 2)
    return 1 + f((n + 1) // 2)

t, l, r = map(int, input().split())
mod = int(1e9) + 7

# Initialize dp array
dp = [[0] * (l + 1) for _ in range(l + 1)]

for i in range(l):
    for j in range(i, l + 1):
        if i == 0:
            dp[i][j] = f(j)
        else:
            dp[i][j] = min(dp[i - 1][k] + 1 for k in range(2, j + 1))
        dp[i][j] %= mod

# Calculate the expression
res = sum(ti * dp[0][li + ti - 1] for ti, li in zip(map(int, input().split()), range(l, r + 1))) - l * f(r)
print(res % mod)
