import sys

# Read input from stdin
n, t = map(int, input().split())
fraction = [int(x) for x in input().split()]

dp = [0] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    if int(fraction[i-1]) < 5:
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1], dp[i-1] + 9.99 * (10**(n-i)))

# Print the maximum possible grade to stdout
print(max(0, dp[-1]))
