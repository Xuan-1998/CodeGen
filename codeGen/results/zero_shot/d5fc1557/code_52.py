def longestSubarray(nums):
    n = len(nums)
    ones = [i for i in range(n) if nums[i] == 1]
    max_length = 0
    current_length = 0
    for i in range(len(ones)):
        if i > 0 and ones[i] - ones[i-1] > 1:
            current_length = 1
        else:
            current_length += 1
        max_length = max(max_length, current_length)
    return max_length
