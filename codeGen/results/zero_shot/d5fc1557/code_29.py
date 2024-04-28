def longestSubarray(nums):
    n = len(nums)
    res = 0
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            res = max(res, ones)
            ones = 0
    return max(res, ones)

n = int(input())
nums = list(map(int, input().split()))
print(longestSubarray(nums))
