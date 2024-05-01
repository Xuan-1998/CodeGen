def subsetSumDivisible(nums, m):
    dp = [[False] * (m + 1) for _ in range(len(nums) + 1)]
    
    # Base case: there is a subset that sums to 0 with any numbers included
    for i in range(m + 1):
        dp[0][i] = True
    
    for i in range(1, len(nums) + 1):
        for j in range(m + 1):
            if nums[i - 1] <= j:
                # Check if there is a subset that sums to (j - nums[i-1]) and includes all numbers up to i-1
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i][j]
            else:
                # If the current number exceeds j, skip it
                dp[i][j] = dp[i-1][j]
    
    return dp[-1][-1]

# Example usage:
n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(subsetSumDivisible(nums, m))
