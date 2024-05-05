import sys

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        if j == 0:
            dp[i][j] = i
        else:
            min_digits = sys.maxsize
            for k in range(10**(i - 1), 10**i):
                new_digits = len(str(k)) + dp[k % 10][j - 1]
                min_digits = min(min_digits, new_digits)
            dp[i][j] = min_digits

print(dp[n][m])
