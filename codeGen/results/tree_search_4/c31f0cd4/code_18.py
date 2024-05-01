import sys
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

dp = defaultdict(bool)
dp[0] = True  # base case

for num in nums:
    for i in range(sum(nums), -1, -num):
        dp[i] = dp.get(i, False) or dp[i-num]

print(*sorted({k for k in dp if dp[k]}))
