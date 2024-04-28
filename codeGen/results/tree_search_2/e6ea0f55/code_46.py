def maxSum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = nums[i - 1]
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + nums[i - 1], dp[i - 1][k - j] + nums[i - 1])

    return max([dp[i][k] for i in range(1, n + 1)])

if __name__ == "__main__":
    nums = [list(map(int, input().split()))]
    k = int(input())
    print(maxSum(*nums[0], k))
