def longest_subarray(nums):
    n = len(nums)
    max_length = 0
    curr_length = 0
    
    for i in range(n):
        if nums[i] == 1:
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 0
            
    return max_length - (n == 0)

n = int(input())
nums = [int(i) for i in input().split(',')]
print(longest_subarray(nums))
