def longest_ones(n):
    n = int(input())
    nums = [int(x) for x in input().split()]
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count - (1 if len(nums) > max_count else 0)
