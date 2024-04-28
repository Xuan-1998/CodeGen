def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = nums[i]
    
    for j in range(1, k + 1):
        for i in range(j, n):
            if i - j >= 0:
                dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-j-1][j-1])
            else:
                dp[i][j] = nums[i]

    return max(sum(subsequence) for subsequence in dp)

# Test the function
nums = list(map(int, input().split()))
k = int(input())
print(max_sum_subsequence(nums, k))
