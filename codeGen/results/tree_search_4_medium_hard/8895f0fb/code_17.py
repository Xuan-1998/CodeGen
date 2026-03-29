import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(10):
        for j in range(10):
            if i + j >= 10:
                dp[i][j] = 1
            elif i < 5 and j < 5:
                dp[i][j] = 0
            else:
                dp[i][j] = 0.5

    expected_carries = sum([sum(row) for row in dp]) / (N ** 2)
    print(f"{expected_carries:.6f}")
