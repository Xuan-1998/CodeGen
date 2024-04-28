import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[max(0, i - k)], nums[i - 1]) + nums[i]

print(max(dp))
