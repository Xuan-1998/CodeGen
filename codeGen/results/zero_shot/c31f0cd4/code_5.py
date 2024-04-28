n = int(input())
nums = list(map(int, input().split()))
total_sum = sum(nums)
dp = [[[] for _ in range(total_sum + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, total_sum + 1):
        if nums[i - 1] <= j:
            dp[i][j] = dp[i - 1][j] | (dp[i - 1][j - nums[i - 1]] + [nums[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]

print(*sorted(set(sum(subset) for subset in dp[-1])), sep=' ')
