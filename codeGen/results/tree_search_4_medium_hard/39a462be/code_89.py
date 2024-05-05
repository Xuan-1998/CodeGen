def solve():
    n, m = map(int, input().split())
    A = input()
    B = input()

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 4 * (dp[i - 1][j - 1] + 1) - i - j
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return max(max(row) for row in dp)

print(solve())
