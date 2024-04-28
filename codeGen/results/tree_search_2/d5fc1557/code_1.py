def longestSubarray(nums):
    n = len(nums)
    memo = {0: 0}
    max_length = 0

    for i in range(1, n + 1):
        if nums[i-1] == 1:
            max_length = max(max_length, memo.get(i-1, 0) + 1)
        else:
            max_length = max(max_length, memo.get(i-1, 0))
        memo[i] = max_length

    return max_length
