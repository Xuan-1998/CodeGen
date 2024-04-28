def longest_subarray(nums):
    n = len(nums)
    max_length = curr_length = 0

    for i in range(n):
        if nums[i] == 1:
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:  # num is 0
            curr_length = 0

    # Remove the last element and update max_length
    if nums[-1] == 1:
        return max_length - 1
    else:
        return max_length
