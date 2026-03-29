from collections import defaultdict

def expected_non_zero_carries(N):
    dp = [[0] * (N + 1) for _ in range(11)]

    for k in range(10):
        if k == 0:
            dp[k][0] = 1
        else:
            dp[k][0] = dp[k-1][0]

    for n in range(1, N+1):
        for k in range(N+1):
            if n > 0 and k < N:
                dp[k][n] = (dp[0][n-1] + dp[9][n-1]) / 2
            elif n == 0:
                dp[k][n] = 1

    return sum(sum(row) for row in dp) / (10**N * N)

T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_non_zero_carries(N))
