import sys

n, t = map(int, input().split())
fractional_part = [int(x) for x in input().split('.')]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i <= t:
        dp[i] = max(dp[i-1], int(str(fractional_part[0]) + '.' + ''.join(map(str, fractional_part[1:i]))))
    else:
        dp[i] = dp[i-1]

print(int(dp[-1]))
