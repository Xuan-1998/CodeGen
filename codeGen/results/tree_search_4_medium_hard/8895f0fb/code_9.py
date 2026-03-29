import sys

T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[i - 1] + B[j - 1] >= 10:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    carry_count = sum(sum(row) for row in dp)
    expected_carries = carry_count / (N ** 2)

    print(f"{expected_carries:.6f}")
