n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(sum(nums) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(sum(nums) + 1):
        if j < nums[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]] + [nums[i - 1]]) if not dp[i - 1][j] else dp[i - 1][j - nums[i - 1]] + [nums[i - 1]]
print(*sorted(set(dp[-1][-1])))
