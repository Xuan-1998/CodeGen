def maximum_ones(nums):
    n = len(nums)
    max_length = 0
    
    left, right = 0, 0
    while right < n:
        if nums[right] == 1:
            right += 1
        else:
            if right - left > max_length:
                max_length = right - left
            right += 1
            left = right
            
    return max_length

# example usage
nums = list(map(int, input().split()))
print(maximum_ones(nums))
