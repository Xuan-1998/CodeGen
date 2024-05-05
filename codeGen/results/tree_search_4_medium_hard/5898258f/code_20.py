def solve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if abs(A[j] - x) > abs(A[i - 1] - x):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] ^ A[j])

    return max(dp[-1])

print(solve())
