def longestSubarray(nums):
    n = len(nums)
    ones = [i for i in range(n) if nums[i] == 1]
    max_len = 0
    for i in range(len(ones)):
        count = 1
        while i + 1 < len(ones) and ones[i+1] - ones[i] == 1:
            count += 1
            i += 1
        max_len = max(max_len, count)
    return max_len
