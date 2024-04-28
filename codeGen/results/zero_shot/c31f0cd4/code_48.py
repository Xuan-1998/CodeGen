import itertools
from collections import defaultdict

n = int(input())
nums = [int(x) for x in input().split()]

total_sum = sum(nums)
dp = [0] * (total_sum + 1)

for i in range(2 ** n):
    temp_sum = 0
    subset = []
    for j in range(n):
        if ((i >> j) & 1):
            subset.append(nums[j])
            temp_sum += nums[j]
    dp[temp_sum] += 1

ans = [i for i in range(total_sum + 1) if dp[i]]
print(' '.join(map(str, ans)))
