n = int(input())
nums = list(map(int, input().split()))
dp = [[[] for _ in range(n+1)] for _ in range(101)]
for i in range(1, n+1):
    for j in range(nums[i-1], 101):
        dp[j][i] = [x + nums[i-1] for x in dp[j-nums[i-1]][i-1]]
print(*sorted({sum(subset) for subset in (dp[sum(dp)][-1])}), sep=' ')
