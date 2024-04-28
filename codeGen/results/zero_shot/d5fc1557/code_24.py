def longest_ones(nums):
    n = len(nums)
    max_length = 0
    count = 0
    
    for i in range(n):
        if nums[i] == 1:
            count += 1
            max_length = max(max_length, count)
        else:
            count = 0
    
    return max_length - (n - count)
