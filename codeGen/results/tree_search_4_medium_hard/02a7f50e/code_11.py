import sys

n = int(input())
dp = [[0] * 1000001 for _ in range(n + 1)]

for j in range(1, 1000001):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, 1000001):
        min_destroyed = sys.maxsize
        for k in range(i):
            if j >= k:
                min_destroyed = min(min_destroyed, dp[k][j - 1] + (i - k))
        dp[i][j] = min_destroyed

result = 0
for i in range(n):
    result += max(0, dp[i][dp[i].index(max(dp[i]))] - i)

print(result)
