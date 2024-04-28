def longestSubarray(nums):
    n = len(nums)
    res = 0
    cur_len = 0
    ones = 0
    
    for i in range(n):
        if nums[i] == 1:
            ones += 1
            cur_len += 1
        else:
            cur_len = 0
        
        res = max(res, cur_len)
    
    return res - (ones > 0)

