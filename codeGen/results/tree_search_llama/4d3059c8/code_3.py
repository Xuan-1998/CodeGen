def pivotIndex(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    left_sum = 0
    
    for i in range(n):
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += nums[i]

    return -1
