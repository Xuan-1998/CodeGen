def longestSubarray(nums):
    n = len(nums)
    res, start = 0, 0
    for end in range(n):
        while start <= end and (start == 0 or nums[start - 1] != nums[end]):
            start += 1
        res = max(res, end - start + 1)
    return res if res > 0 else 0

n = int(input())
nums = [int(x) for x in input().split()]
print(longestSubarray(nums))
