from collections import defaultdict

def max_sum_subsequence(nums, k):
    dp = [[0] * (k + 1) for _ in range(len(nums) + 1)]
    memo = defaultdict(int)

    for i in range(1, len(nums) + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = nums[i-1]
            else:
                for k in range(max(0, i-j), i):
                    dp[i][j] = max(dp[i][j], memo[dp[k][j-1]] - nums[k] + nums[i-1])
                    memo[dp[i][j]] = dp[i][j]

    return dp[-1][-1]
