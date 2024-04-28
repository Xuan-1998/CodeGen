nums = list(map(int, input().split()))
k = int(input())
dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]
for i in range(1, len(nums) + 1):
    for j in range(1, min(i, k) + 1):
        if i - j >= 0:
            dp[i][j] = max(dp[i-1][j-1] + nums[i-1], dp[i-1][j])
print(max(dp[-1]))
