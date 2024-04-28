def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    
    # Initialize the base case: maximum sum of subsequences with no gaps (i.e., consecutive elements) is the maximum value in nums.
    for i in range(n):
        dp[i+1] = max(dp[i], nums[i])
        
    # Calculate the maximum sum of subsequences ending at each index, considering all possible differences between indices up to k
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i - j - 1 >= 0:
                dp[i] = max(dp[i], dp[i-j-1] + nums[i])
                
    return dp[-1]

# Read input from stdin
nums = list(map(int, input().split()))
k = int(input())

print(maxSumOfSubsequence(nums, k))
