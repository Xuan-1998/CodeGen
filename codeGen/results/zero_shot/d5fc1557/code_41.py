def longest_ones(nums):
    n = len(nums)
    ones_count = nums.count('1')
    if ones_count == 0:
        return 0
    max_length = 0
    current_length = 0
    for num in nums:
        if num == '1':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

n = int(input())
nums = [str(num) for num in input().split()]
print(longest_ones(nums))
