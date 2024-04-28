def longestSubarray(nums):
    ones = 0
    for i, x in enumerate(nums):
        if x == 1:
            ones += 1
        else:
            break

    max_length = ones
    zeros = 0
    for i, x in enumerate(reversed(nums)):
        if x == 0:
            zeros += 1
        else:
            max_length = max(max_length, ones + zeros)
            break

    return max_length
