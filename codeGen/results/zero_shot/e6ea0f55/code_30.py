from bisect import bisect_left, bisect_right
n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][i] = nums[i-1]
    for j in range(i):
        if nums[j-1] + k >= nums[i-1]:
            dp[i][j] = max(dp[i][j], dp[j][j] + nums[i-1])
        else:
            dp[i][j] = max(dp[i][j], dp[j][i])

print(max(dp[n]))
