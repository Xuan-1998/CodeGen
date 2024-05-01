def longest_subarray(nums):
    max_len = 0
    end_idx = -1

    for i, num in enumerate(nums):
        if num == 1:
            max_len += 1
            end_idx = i
        else:  # num == 0
            if nums[end_idx] == 1:  # subarray ending at end_idx has more than one 1's
                max_len += 1
                end_idx = i
            else:  # subarray ending at end_idx contains only one 1
                max_len = 1
                end_idx = i

    return max_len
