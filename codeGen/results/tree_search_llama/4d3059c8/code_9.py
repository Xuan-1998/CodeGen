def pivotIndex(nums):
    n = len(nums)
    total_sum = sum(nums)
    
    # Calculate prefix sum and store it in a list
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Iterate through the array to find the pivot index
    for i in range(n):
        left_sum = prefix_sum[i] - nums[i]
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            return i
    
    return -1
