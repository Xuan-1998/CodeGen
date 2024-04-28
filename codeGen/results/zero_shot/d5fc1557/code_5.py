def longest_subarray(nums):
    n = len(nums)
    one_count = 0
    max_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            one_count += 1
        else:
            max_length = max(max_length, one_count)
            one_count = 0
    
    return max(max_length, one_count)

n = int(input())
nums = [int(x) for x in input().split()]
print(longest_subarray(nums))
