def longestSubarray(nums):
    n = len(nums)
    one_count = sum(nums)
    if one_count == 0:
        return 0
    max_length = 0
    for i in range(n):
        ones = 0
        for j in range(i, n):
            if nums[j] == 1:
                ones += 1
            else:
                break
        max_length = max(max_length, ones)
    return max_length

n = int(input())
nums = [int(x) for x in input().split(',')]
print(longestSubarray(nums))
