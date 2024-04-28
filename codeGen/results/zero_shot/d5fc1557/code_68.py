def longest_subarray(nums):
    n = len(nums)
    ones_count = nums.count(1)
    zeros_count = n - ones_count
    max_length = 0
    
    for i in range(n):
        current_ones = 0
        for j in range(i, n):
            if nums[j] == 1:
                current_ones += 1
            else:
                break
        if current_ones > max_length:
            max_length = current_ones
    
    return max_length
