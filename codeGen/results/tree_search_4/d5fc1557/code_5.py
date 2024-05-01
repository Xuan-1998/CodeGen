def longestSubarray(nums):
    max_length = 0
    current_length = 0

    for num in nums:
        if num == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length - 1
