n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(n + 1)] for _ in range(sum(nums) + 1)]
for i in range(1, n + 1):
    for j in range(i, sum(nums) + 1):
        if nums[i - 1] <= j:
            dp[j][i] = list(set(dp[j - nums[i - 1]][i - 1] + [j]))
        else:
            dp[j][i] = dp[j][i - 1]
print(' '.join(map(str, sorted([item for sublist in dp[-1][n] for item in sublist]))))
