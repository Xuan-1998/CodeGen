def longest_subarray(nums):
    n = len(nums)
    max_length = 0
    for i in range(n):
        length = 1
        while i + length < n and nums[i] == nums[i + length]:
            length += 1
        max_length = max(max_length, length)
    return max_length
