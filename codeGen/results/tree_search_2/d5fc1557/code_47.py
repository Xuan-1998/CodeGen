def longestSubarray(nums):
    n = len(nums)
    max_length = 0
    
    left = right = 0
    count = 0
    
    for i in range(n):
        if nums[i] == 1:
            count += 1
        else:
            if count > 0:
                max_length = max(max_length, count)
            count = 0
        
        if i < n - 1 and (nums[i + 1] == 0 or nums[n - 1] == 0):
            right = i
    
    if count > 0:
        max_length = max(max_length, count)
    
    return max_length
