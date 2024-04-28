def longestOnes(nums):
    n = len(nums)
    ones = 0
    max_length = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            max_length = max(max_length, ones)
            ones = 0
    return max(max_length, ones)
