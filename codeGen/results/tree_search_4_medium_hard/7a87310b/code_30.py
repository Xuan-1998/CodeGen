import sys

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: there is one way to form the identity matrix with positive determinant
    for d in range(1, n + 1):
        dp[1][d] = 1

    for i in range(2, n + 1):
        for d in range(1, min(i, n) + 1):
            if d > 0:
                dp[i][d] = sum(dp[k][d - 1] for k in range(1, i))
            else:
                dp[i][d] = 0

    print(dp[n][n])
