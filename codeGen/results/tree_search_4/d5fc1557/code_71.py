def longest_subarray(nums):
    max_length = 0
    current_streak = 0

    for num in nums:
        if num == 1:
            current_streak += 1
            max_length = max(max_length, current_streak)
        else:  # num == 0
            current_streak = 0

    return max_length - (0 in nums)  # subtract 1 if the original array had a 0
