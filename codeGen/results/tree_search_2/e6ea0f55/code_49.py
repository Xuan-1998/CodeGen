def max_sum_of_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])

    return dp[n][k]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    print(max_sum_of_subsequence(nums, k))
