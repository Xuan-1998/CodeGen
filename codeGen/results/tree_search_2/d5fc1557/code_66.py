def longest_subarray(nums):
    n = len(nums)
    max_len = 0
    streak = [0] * (n + 1)  # Initialize with zeros

    for i in range(n):
        if nums[i] == 1:  # Found a 1, update the current streak
            streak[i + 1] = streak[i] + 1
        else:  # Found a 0, reset the current streak and update max_len
            max_len = max(max_len, streak[i])
            streak[i + 1] = 0

    return max(max_len, streak[-1]) if streak[-1] > 0 else 0
