def longestSubarray(nums):
    n = len(nums)
    ans = 0
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            ans = max(ans, ones)
            ones = 0
    return max(ans, ones)

n = int(input())
nums = [int(x) for x in input().split()]
print(longestSubarray(nums))
