import sys

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Fill the DP table
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i > 0 and j > 0:
                dp[i][j] = 1 + dp[max(i-1, j-1)][min(i-1, j-1)]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]

    # Calculate the expected number of non-zero carries
    expected_carries = sum([sum(row) for row in dp]) / (N**2)

    print(f"{expected_carries:.6f}")
