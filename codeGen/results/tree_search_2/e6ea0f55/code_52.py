def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [(0, 0) for _ in range(n+1)]
    
    for i in range(1, n+1):
        if i <= k:
            dp[i] = (max(dp[j][0] + nums[i-1] for j in range(max(0, i-k), i)), i-1)
        else:
            dp[i] = max((dp[j][0] + nums[i-1], i-1) for j in range(i-k, i))
    
    return max(dp[n][0], default=0)

# Receive inputs from stdin and print the answer to stdout
nums = [int(x) for x in input().split()]
k = int(input())
print(maxSumSubsequence(nums, k))
