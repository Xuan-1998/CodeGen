dp = [[0] * (max(A) + 1) for _ in A]
for i, x in enumerate(A):
    dp[i][x] += 1
    bad_count = sum(1 for y in A[:i+1] if y % y != 0)
    for j in range(min(i+1, max(A)+1), 0, -1):
        if (j > 1 and i >= x) or (x < j):
            dp[i][j] += dp[i-x][j-1]
        else:
            dp[i][j] += dp[i-x-1][j-1]
        if bad_count % j == 0:
            dp[i][j] -= dp[i-x-1][j]
    for j in range(min(i+2, max(A)+1), min(j+1, max(A)+1), -1):
        if (j > 1 and i >= x) or (x < j):
            dp[i][j] += dp[i-j][j-1]
        else:
            dp[i][j] += dp[i-j-1][j-1]
    for j in range(2, min(i+3, max(A)+1)):
        if (j > 1 and i >= x) or (x < j):
            dp[i][j] += dp[i-j][j-1]
        else:
            dp[i][j] += dp[i-j-1][j-1]

print(sum(dp[-1]) % (10**9 + 7))
