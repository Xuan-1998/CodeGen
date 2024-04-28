def longest_subarray(nums):
    memo = {}

    def dp(i, ones, zeros):
        if (i, ones, zeros) in memo:
            return memo[(i, ones, zeros)]

        if i == len(nums):
            return 0

        if nums[i] == 1:
            ones += 1
        else:
            zeros += 1

        res = dp(i + 1, ones, zeros)
        if ones > 0 and (ones, zeros) not in memo:
            res = max(res, dp(i - 1, ones - 1, zeros) + 1)

        memo[(i, ones, zeros)] = res
        return res

    result = dp(0, 0, 0)
    for i in range(len(nums)):
        if nums[i] == 1:
            result = max(result, dp(i, 0, 0) + 1)

    return result
