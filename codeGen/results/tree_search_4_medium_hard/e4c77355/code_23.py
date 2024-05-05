def lengthOfLIS(nums):
    n = len(nums)
    dp = [[1] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if nums[j - 1] <= nums[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    return max(max(row) for row in dp[:-1])

# Example usage:
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))
