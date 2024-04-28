def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = max(dp[i-1], nums[i-1])
        else:
            dp[i] = max(dp[i-1], nums[i-1] + dp[max(0, i-k)])

    return dp[-1]

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(maxSumSubsequence(nums, k))
