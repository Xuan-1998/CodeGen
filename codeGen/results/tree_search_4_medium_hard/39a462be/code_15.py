def max_similarity_score():
    n, m = map(int, input().split())
    A = input()
    B = input()

    dp = [[[0 for _ in range(m+1)] for _ in range(n+1)]]  # Initialize DP array

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[0][i][j] = dp[0][i-1][j-1] + 4  # Add 4 to the LCS length
            else:
                dp[0][i][j] = max(dp[0][i-1][j], dp[0][i][j-1])  # Update DP array

    return dp[0][n][m]

print(max_similarity_score())
