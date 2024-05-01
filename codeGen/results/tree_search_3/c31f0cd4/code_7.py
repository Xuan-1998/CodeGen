def find_distinct_sums(nums):
    n = len(nums)
    dp = [[False] * (sum(nums) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, sum(nums) + 1):
            if nums[i - 1] <= j:
                dp[i][j] = any(dp[k][j - num] for k in range(i))
            else:
                dp[i][j] = False

    return [i for i in range(sum(nums) + 1) if dp[n][i]]

# Example usage
nums = list(map(int, input().split()))
print(" ".join(map(str, find_distinct_sums(nums))))
