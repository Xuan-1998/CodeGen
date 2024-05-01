from collections import defaultdict

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    max_sum = 0
    
    # Initialize a dictionary to store the maximum values for each subarray
    dp = defaultdict(int)
    
    # Initialize the current maximum value and sum
    curr_max = float('-inf')
    curr_sum = 0
    
    # Iterate over the array
    for i, val in enumerate(arr):
        # Update the current maximum value and sum
        curr_max = max(curr_max, val)
        curr_sum += val
        
        # If we've reached the end of a subarray or it's too long, update the dp dictionary
        if (i + 1) % k == 0:
            dp[i] = curr_max * k
            curr_max = float('-inf')
            curr_sum = 0
    
    # Calculate the maximum sum after partitioning
    for i in range(n):
        max_sum = max(max_sum, dp.get(i, 0))
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(max_sum_after_partitioning(arr, k))  # Output: 18 (partitioned as [6, 6, 6])
