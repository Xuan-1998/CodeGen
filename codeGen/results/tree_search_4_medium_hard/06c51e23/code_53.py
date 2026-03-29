import sys

n, t = map(int, input().split())
fraction = float('0.' + '0' * (n-1) + '9')

dp = [0] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    if i < n:
        round_here = max(dp[i-1], fraction % 10)
        not_round_here = dp[i-1]
        if round_here >= 5 or round_here == 4.5:
            round_here = 9.99 * (10**(n-i))
        dp[i] = max(round_here, not_round_here)
    else:
        dp[i] = 9.99

print(int(max(dp)))
