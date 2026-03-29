import sys

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    A = [int(x) for x in input().strip()]
    B = [int(x) for x in input().strip()]

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    total_carries = 0

    for i in range(1, N + 1):
        for j in range(N + 1):
            if A[N - i] + B[N - j] >= 10:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j]

    for i in range(1, N + 1):
        total_carries += sum(dp[i])

    expected_carries = total_carries / ((N + 1) ** 2)
    print('{:.6f}'.format(expected_carries))
