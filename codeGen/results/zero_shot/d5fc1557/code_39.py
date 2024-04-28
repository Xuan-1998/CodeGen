def longest_ones(nums):
    n = len(nums)
    max_length = 0
    current_count = 0
    
    for i in range(n):
        if nums[i] == 1:
            current_count += 1
            max_length = max(max_length, current_count)
        else:
            current_count = 0
    
    return max_length

n = int(input())
nums = list(map(int, input().split()))
print(longest_ones(nums))
