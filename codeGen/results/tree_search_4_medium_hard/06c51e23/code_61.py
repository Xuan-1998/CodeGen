import sys

# Read input from stdin
n, t = map(int, input().split())
fractional_part = [int(x) for x in input().split()]


dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i > t:
        dp[i] = sum(fractional_part[:i])
    else:
        diff = abs(sum(fractional_part[:i]) - round(sum(fractional_part[:i])))
        if diff >= 0.5:
            dp[i] = round(sum(fractional_part[:i]))
        else:
            dp[i] = max(dp[i-1], round(sum(fractional_part[:i])))

print(int(round(dp[n])))
