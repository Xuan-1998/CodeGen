def maximum_ones(nums):
    n = len(nums)
    left = [0] * n
    right = [0] * n
    
    for i in range(1, n):
        if nums[i] == 1:
            left[i] = max(left[i-1], 1)
            right[i] = max(right[i-1], left[i-1]+1)
        else:
            left[i] = 0
            right[i] = 0
    
    return max(max(right), max(left))
