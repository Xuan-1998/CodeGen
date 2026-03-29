def solve():
    n, m = map(int, input().split())
    A = input()
    B = input()

    # Initialize the 2D DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 4
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximum similarity score over all pairs of substrings
    return max(max(row) for row in dp)

print(solve())
