def max_sum(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i+1] = max(dp[i], nums[i])
    
    res = float('-inf')
    for i in range(k+1):
        temp = dp[i]
        for j in range(i+k, n+1):
            temp += nums[j-1]
            res = max(res, temp)
    
    return res

import sys
n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(max_sum(nums, k))
