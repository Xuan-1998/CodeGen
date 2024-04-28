def longestSubarray(nums):
    memo = {}
    def helper(ones, zeros):
        if (ones, zeros) in memo:
            return memo[(ones, zeros)]
        res = 0
        if ones > 0 and zeros == 0:
            res = 1
        elif ones > 0 and zeros > 0:
            res = 1 + helper(ones - 1, zeros - 1)
        memo[(ones, zeros)] = res
        return res

    n = len(nums)
    max_len = 0
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            max_len = max(max_len, helper(ones, 0))
            ones = 0

    return max(len(str(nums)), max_len)
