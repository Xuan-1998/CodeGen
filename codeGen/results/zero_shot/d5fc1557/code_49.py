def longest_ones(nums):
    n = len(nums)
    max_len = 0
    count = 0
    
    for i in range(n):
        if nums[i] == 1:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    
    return max_len - (n - len(nums) // 2) if n % 2 != 0 and max_len > n // 2 else max_len

import sys
n = int(input())
nums = [int(x) for x in input().split()]
print(longest_ones(nums))
