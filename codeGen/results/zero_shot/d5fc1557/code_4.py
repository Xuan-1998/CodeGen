def longest_subarray(nums):
    n = len(nums)
    ones = 0
    max_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            ones += 1
            max_length = max(max_length, ones)
        else:
            ones = 0
    
    return max_length

n = int(input())
nums = [int(x) for x in input().split()]
print(longest_subarray(nums))
