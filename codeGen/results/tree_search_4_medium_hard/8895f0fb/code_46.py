import sys

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]

    # initialize base case
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(10):
            if j > 4:
                dp[i][j] += 1
            else:
                dp[i][j] += (j == 4) * (5 - j)
            for k2 in range(j + 1, 10):
                dp[i-1][k2] += dp[i-1][j]
                dp[i][k2] += dp[i-1][j]

    res = sum(sum(row) for row in dp) / (N+1)**2
    print(f"{res:.9f}")
