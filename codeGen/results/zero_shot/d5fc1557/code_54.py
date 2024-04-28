def longestSubarray(nums):
    n = len(nums)
    ones = [i for i in range(n) if nums[i] == 1]
    max_len = 0
    last_ones_index = -1
    
    for end in range(n):
        while ones and ones[0] <= end:
            last_ones_index = ones.pop(0)
        
        max_len = max(max_len, end - last_ones_index)
    
    return max_len
