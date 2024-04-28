import sys
from collections import defaultdict

m, N = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[0] = 1

for num in nums:
    for i in range(N, num - 1, -1):
        dp[i] += dp[i - num]
    dp[i] %= 10**9 + 7

print(dp[N])
