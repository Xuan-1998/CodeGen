def longest_subarray(nums):
    n = len(nums)
    res = 0
    ones_count = 0
    
    for i in range(n):
        if nums[i] == 1:
            ones_count += 1
        else:
            if ones_count > 0:
                res = max(res, ones_count)
                ones_count = 0
    return max(ones_count, res)
