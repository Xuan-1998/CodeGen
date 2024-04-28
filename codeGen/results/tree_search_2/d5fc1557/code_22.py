def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    
    ones_count = sum(1 for num in nums if num == 1)
    zeros_count = n - ones_count
    
    current_ones = ones_count
    max_length = 0
    
    for i, num in enumerate(nums):
        if num == 1:
            current_ones -= 1
        else:
            zeros_count -= 1
        
        dp[i + 1] = min(dp[i], current_ones) + 1
        
        max_length = max(max_length, dp[i + 1])
    
    return max_length - 1

# Read the input from standard input
n = int(input())
nums = [int(num) for num in input().split()]

print(longest_subarray(nums))
