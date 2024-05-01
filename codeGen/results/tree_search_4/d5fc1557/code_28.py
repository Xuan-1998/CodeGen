===BEGIN CODE===
def longestSubarray(nums):
    n = len(nums)
    dp = {(i, 0): 0 for i in range(n)}
    max_length = 0
    for i in range(1, n):
        if nums[i] == 0:
            dp[(i, 0)] = max(dp.get((i-1, 0), 0), 0)
        else:
            ones = 0
            for j in range(i, -1, -1):
                if nums[j] == 1:
                    ones += 1
                else:
                    break
            dp[(i, 0)] = max(dp.get((i-1, 0), 0), ones)
            max_length = max(max_length, dp[(i, 0)])
    return max_length

===END CODE===
