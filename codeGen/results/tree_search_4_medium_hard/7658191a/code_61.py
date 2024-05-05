code
n, k, z = map(int, input().split())
scores = list(map(int, input().split()))
dp = [[0] * (z + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    dp[i][0] = max(dp[i-1][0], scores[i])
    for j in range(1, min(i, z) + 1):
        if j == 1:
            dp[i][j] = max(dp[i-1][j-1], scores[i]) + scores[i]
        else:
            dp[i][j] = max(dp[i-z][z-1], dp[i-1][j-1]) + scores[i]

print(max(dp[k]))
