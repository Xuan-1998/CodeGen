def maximum_ones(nums):
    max_len = 0
    curr_streak = 0
    prev_one = False

    for num in nums:
        if num == 1 and not prev_one:
            curr_streak += 1
        elif num == 0 and prev_one:
            max_len = max(max_len, curr_streak)
            curr_streak = 0
        prev_one = num == 1

    return max(max_len, curr_streak)
