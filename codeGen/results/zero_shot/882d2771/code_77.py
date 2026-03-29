import sys

t, l, r = map(int, input().split())

dp = [0] * (r+1)
for i in range(2, r+1):
    dp[i] = min(dp[j] + 1 for j in range(i)) if i > 1 else 0

f_l = sum(t*k*dp[k] for k in range(l, r+1)) - l*dp[r]
print(f_l % (10**9 + 7))
