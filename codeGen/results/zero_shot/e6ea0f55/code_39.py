nums = list(map(int, input().split()))
k = int(input())
dp = [[0] * (k + 1) for _ in range(len(nums) + 1)]
for i in range(1, len(nums) + 1):
    dp[i][0] = max(dp[i-1][0], nums[i-1])
    for j in range(1, min(i, k)+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + nums[i-1])
print(max(sum(sub) for sub in dp))
