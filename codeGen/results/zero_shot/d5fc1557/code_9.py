def longestSubarray(nums):
    n = len(nums)
    res = 0
    oneCount = 0
    for i in range(n):
        if nums[i] == 1:
            oneCount += 1
        else:
            if oneCount > res:
                res = oneCount
            oneCount = 0
    return max(res, oneCount)
