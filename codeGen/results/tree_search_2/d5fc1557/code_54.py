def longestSubarray(nums):
    n = len(nums)
    res = 0
    cur = 0

    for i in range(n):
        if nums[i] == 1:
            cur += 1
            res = max(res, cur)
        else:
            cur = 0

    return res - 1

n = int(input())
nums = list(map(int, input().split()))
print(longestSubarray(nums))
