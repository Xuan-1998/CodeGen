import sys

dp = [0] * ((10**5 + 7) // 2)
a, b = map(int, input().split())
for i in range(1, (10**5 + 7) // 2):
    dp[i] = (dp[i-1] + (b % 2 == 1 and a or 0)) % (10**9+7)
print(sum(dp))
