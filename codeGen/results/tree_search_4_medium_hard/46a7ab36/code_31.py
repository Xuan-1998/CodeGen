import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Initialize base cases: there is only one way to form an empty word or a word of length 1
for i in range(n + 1):
    dp[i][0] = 1

for j in range(m + 1):
    dp[0][j] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if 2 * (i - 1) <= n:
            dp[i][j] = dp[i - 1][j - 1] * (n - i + 1) + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] * (n - i + 1) + dp[n - 1][j - 1]

state = sum(dp[-1])
print(state % (10**8 + 7))
