def longest_ones(nums):
    n = len(nums)
    max_length = 0
    for i in range(n):
        current_length = 0
        for j in range(i, n):
            if nums[j] == 1:
                current_length += 1
            else:
                break
        max_length = max(max_length, current_length)
    return max_length

n = int(input())
nums = [int(x) for x in input().split()]
print(longest_ones(nums))
