from bisect import bisect_left
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    dp[i][0] = nums[i]
    
for j in range(1, k + 1):
        current_sum = float('-inf')
        for i in range(j - 1, n):
            current_sum = max(current_sum, dp[i - j + 1][j - 1] + nums[i])
            dp[i][j] = current_sum
print(max(dp[-1]))
