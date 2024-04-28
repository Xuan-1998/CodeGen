n = int(input())
k = int(input())
nums = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = nums[i - 1]
for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        dp[i][j] = max(dp[i][j], dp[i][j - 1] + nums[j])
print(max((dp[i][n] for i in range(n))))
