def longest_subarray(nums):
    n = len(nums)
    ones = 0
    max_length = 0
    left = 0
    
    for right in range(n):
        if nums[right] == 1:
            ones += 1
        
        while ones > 1:
            if nums[left] == 1:
                ones -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
