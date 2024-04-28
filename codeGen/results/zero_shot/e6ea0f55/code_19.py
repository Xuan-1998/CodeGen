def maxSumSubsequence(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = prefix_sum[i]
            else:
                for last_index in range(j - 1, min(i, j)):
                    dp[i][j] = max(dp[i][j], dp[last_index][j - 1] + nums[i])
    
    return max(dp[n])

n = int(input())
k = int(input())
nums = list(map(int, input().split()))
print(maxSumSubsequence(nums, k))
