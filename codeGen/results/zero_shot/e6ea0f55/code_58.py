n = int(input())
k = int(input())
nums = list(map(int, input().split()))
dp = [[0] * (k + 1) for _ in range(n)]
max_sum = float('-inf')
for i in range(1, n):
    for j in range(min(i, k), -1, -1):
        dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-1][j-1])
    max_sum = max(max_sum, dp[-1][-1])
print(max_sum)
