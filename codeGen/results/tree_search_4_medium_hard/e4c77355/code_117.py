def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [[1] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, n), -1, -1):
            if nums[i-1] > nums[j-1]:
                dp[i][0] = max(dp[i][0], dp[j-1][0] + 1)
            for k in range(1, i-j+2):
                if nums[i-1] > nums[j-k]:
                    dp[i][k] = max(dp[i][k], dp[j-k][k-1] + 1)

    return max(max(row) for row in dp)
