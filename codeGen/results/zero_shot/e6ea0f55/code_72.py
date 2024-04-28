nums = list(map(int, input().split()))
k = int(input())
dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
for i in range(1, len(nums) + 1):
    dp[i][i] = nums[i - 1]
    for j in range(i):
        if abs(i - j) <= k:
            dp[i][j] = max(dp[i][j], dp[j][i - 1] + nums[i - 1])
print(max([max(row) for row in dp]))
