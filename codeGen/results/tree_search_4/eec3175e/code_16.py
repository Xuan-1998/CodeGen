# read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# initialize dp table
dp = [[0] * (m + 1) for _ in range(n + 1)]

# base case: empty subset sums to 0 if and only if m == 0
for j in range(m + 1):
    dp[0][j] = 1 if j == 0 else 0

# fill up the dp table
for i in range(1, n + 1):
    for j in range(m + 1):
        if j >= arr[i - 1]:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        else:
            dp[i][j] = dp[i - 1][j]

# answer is the value in the bottom-right corner of the dp table
print(dp[n][m])
