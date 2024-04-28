n = int(input())
k = int(input())
nums = list(map(int, input().split()))
dp = [[0] * (len(nums) + 1) for _ in range(n + 1)]
max_sum = float('-inf')
for i in range(1, len(nums) + 1):
    for j in range(min(i, k) + 1):
        dp[j][i] = max(dp[j][i-1], nums[i-1] + dp[max(0, j-1)][i-1])
max_sum = max(max_sum, dp[k][n])
print(max_sum)
