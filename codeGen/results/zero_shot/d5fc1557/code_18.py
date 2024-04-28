def longest_subarray(nums):
    n = len(nums)
    max_length = 0
    current_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
            
    return max_length

n = int(input())
nums = [int(x) for x in input().split()]
print(longest_subarray(nums))
