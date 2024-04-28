def divisible_subset_sum(n, m, arr):
    # Calculate the total sum of all numbers in the set
    total_sum = sum(arr)
    
    # Initialize a DP array to store whether each sum is divisible by m
    dp = [False] * (total_sum // m + 1)
    
    # Initialize the current sum to 0
    curr_sum = 0
    
    for num in arr:
        # Update the current sum
        curr_sum += num
        
        # If the current sum is greater than or equal to the total sum, break
        if curr_sum >= total_sum:
            break
        
        # For each previous sum that is divisible by m...
        for i in range(curr_sum // m, -1, -1):
            # ...check if adding the current number makes a new sum divisible by m
            if not dp[i] and (curr_sum % m == 0 or dp[curr_sum % m]):
                dp[i + curr_sum // m] = True
        
        # Update the current sum for the next iteration
        curr_sum = max(0, curr_sum - num)
    
    # Return whether there exists a subset with sum divisible by m
    return any(dp)

# Example usage:
n = 5
m = 3
arr = [1, 2, 3, 4, 5]
print(divisible_subset_sum(n, m, arr))  # Output: 1 (because there is a subset with sum divisible by m)
