def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            # If we don't add the current element to the subsequence
            not_include = dp[i - 1][j]
            # If we do add the current element to the subsequence
            include = nums[i - 1] + (dp[i - 2][max(0, j - 1)] if i > 1 else 0)
            dp[i][j] = max(not_include, include)

    return max(dp[n])

# Read input from stdin
nums = list(map(int, input().split()))
k = int(input())

print(maxSumSubsequence(nums, k))
