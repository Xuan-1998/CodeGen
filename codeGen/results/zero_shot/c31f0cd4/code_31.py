n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(sum(nums) + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, sum(nums) + 1):
        if nums[i - 1] <= j:
            dp[i][j] = set(dp[i-1][j-nums[i-1]]).union({j})
        else:
            dp[i][j] = set(dp[i-1][j])

print(*sorted(set.union(*[set(x) for x in dp[-1]])), sep=' ')
