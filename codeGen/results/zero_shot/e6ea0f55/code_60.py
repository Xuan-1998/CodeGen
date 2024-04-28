n = int(input())
nums = list(map(int, input().split()))
k = int(input())

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(min(i, k) + 1):
        dp[i][j] = max(dp[i - 1][j], nums[i - 1])
print(max(sum(sub) for sub in (tuple(nums[i:i + j + 1]) for i in range(n - j) for j in range(k + 1))))
