n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(sum(nums) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(sum(nums) + 1):
        dp[i][j] = []
for i in range(n):
    for j in range(sum(nums) + 1):
        if j < nums[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j] if not dp[i - 1][j] or max(dp[i - 1][j]) > nums[i] 
                        else dp[i - 1][j]) + [nums[i]] + (dp[i - 1][j - nums[i]] if j >= nums[i] and dp[i - 1][j - nums[i]] 
                                                  else [])
print(' '.join(map(str, set(int(sum(x)) for x in dp[-1]))))
