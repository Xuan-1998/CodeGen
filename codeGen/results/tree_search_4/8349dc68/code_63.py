def maxSumAfterPartitioning(nums):
    n = len(nums)
    k = int(input())
    
    # Initialize the DP table with zeros.
    dp = [[0] * (k + 1) for _ in range(n)]

    # Fill in the base case values for dp when j is 1.
    for i in range(n):
        dp[i][1] = nums[i]

    # Calculate the maximum sum up to index i after partitioning into j subarrays.
    for j in range(2, k + 1):
        for i in range(j - 1, n):
            max_val = 0
            for end in range(i - j + 1, i + 1):
                max_val = max(max_val, nums[end])
                dp[i][j] = max(dp[i][j], max_val + dp[end - j + 1][j - 1])

    # Return the maximum sum calculated for the last row of the DP table.
    return dp[-1][-1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(maxSumAfterPartitioning(nums))
