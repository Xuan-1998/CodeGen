# Read input
n = int(input())
m = int(input())
nums = list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(m + 1):
        if nums[i - 1] % m == 0:
            dp[i][k] = True
        elif k % m == 0:
            dp[i][k] = any(dp[j][k // m] for j in range(i))
        else:
            dp[i][k] = any(dp[j][k % m] or (k % m == 0 and nums[i - 1] <= k) for j in range(i))

# Print the answer
print(any(dp[-1][-1]))
