from bisect import *

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], nums[i - 1])
    for j in range(min(i, k) + 1):
        dp[i] = max(dp[i], dp[j - 1] + nums[i - 1])

print(max(dp))
