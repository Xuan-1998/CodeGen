from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

dp = [[False] * (sum(nums) + 1) for _ in range(n + 1)]
dp[0][0] = True  # Base case: empty subset sums to 0

for i in range(1, n + 1):
    for j in range(sum(nums) + 1):
        dp[i][j] = (any(dp[i - 1][k] and k <= j for k in range(j + 1)) or
                    any(dp[k][j - k] for k in range(i)))

ans = [i for i in range(sum(nums) + 1) if dp[n][i]]
print(*ans, sep=' ')
