import sys

def expected_carries(n):
    dp = [[0.0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for k in range(min(i, n), -1, -1):
            if k == 0:
                dp[i][k] = 0
            elif k == i-1:
                dp[i][k] = (9.0 / 10.0) ** (i-k)
            else:
                dp[i][k] = (9.0 / 10.0) * (dp[i-1][k-1] + dp[i-1][k])

    return sum(dp[n][k] for k in range(n+1))

T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
