def longestSubarray(nums):
    n = len(nums)
    ans = 0
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            if ones > 0:
                ans = max(ans, ones)
                ones = 0
    return ans + (ones > 0)

import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
print(longestSubarray(nums))
