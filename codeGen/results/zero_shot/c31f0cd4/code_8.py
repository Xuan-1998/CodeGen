n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(sum(nums) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, sum(nums) + 1):
        if nums[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j] if not dp[i - 1][j] else dp[i - 1][j]) + [nums[i - 1]]
print(' '.join(map(str, sorted({sum(subset) for subset in set(tuple(sorted(subset))) for subset in dp[-1]}))))
