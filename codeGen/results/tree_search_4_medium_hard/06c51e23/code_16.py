import sys
from collections import defaultdict

dp = defaultdict(int)
t, n = map(int, input().split())
frac = float(input())

def calculate_dp(i):
    if i == 0:
        return 0
    digit = int(10**i * (frac - int(frac * 10**n)))
    t_new = max(0, t - 1)
    dp[i] = max(dp.get(i-1, 0), calculate_dp(i-1) + min(t_new//10, digit))
    return dp[i]

print(calculate_dp(n))
