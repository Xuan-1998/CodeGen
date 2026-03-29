def longest_increasing_subsequences(nums):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    prev = [-1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if nums[j - 1] < nums[i - 1]:
                dp[i][j] = min(dp[i - 1][k] + 1 for k in range(j)) or dp[i - 1][j]
            else:
                dp[i][j] = max(0, dp[i - 1][j])
        prev[i] = i

    max_length = max(len(subsequence) for subsequence in set(tuple(range(i, n + 1)) for i in range(n + 1)))
    count = sum(1 for _ in set(tuple(range(i, n + 1)) for i in range(n + 1)) if len(_[0]) == max_length)
    return count
