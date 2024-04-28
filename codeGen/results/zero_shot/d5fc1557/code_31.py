def longest_subarray(nums):
    n = len(nums)
    res = 0
    count = 0
    for i in range(n):
        if nums[i] == '1':
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(res, count)

n = int(input())
nums = [i for i in input().split(',')]
print(longest_subarray(nums))
