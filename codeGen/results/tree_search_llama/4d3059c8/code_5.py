def pivotIndex(nums):
    # Initialize an empty dictionary to store the cumulative sums
    cum_sums = {0: 0}
    
    # Initialize the cumulative sum
    cum_sum = 0
    
    # Iterate through the array and update the hash map with the current index and cumulative sum
    for i, num in enumerate(nums):
        cum_sum += num
        
        # Check if the left sum is equal to the right sum
        if cum_sum - cum_sums.get(i-1, 0) == nums[i]:
            return i
        
        # Update the hash map with the current index and cumulative sum
        cum_sums[i+1] = cum_sum
    
    # If no pivot index is found, return -1
    return -1

