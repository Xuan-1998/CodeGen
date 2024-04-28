def longestSubarray(nums):
    n = len(nums)
    one_count = 0
    max_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            one_count += 1
        else:
            if one_count > 0:
                max_length = max(max_length, one_count)
            one_count = 0

    if one_count > 0:
        return one_count
    else:
        return 0
