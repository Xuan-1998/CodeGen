import sys

n, t = map(int, input().split())
fraction = float('0.' + '9' * n)

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if int((10 ** (i - 1)) * fraction) <= 4:
        dp[i] = max(dp[i-1], dp[i-1] + (9.99 / (10 ** (n - i))))
    else:
        dp[i] = max(dp[i-1], dp[i-1] + (0.01 / (10 ** (n - i))))

print(int(fraction + dp[-1]))
