def max_similarity_score():
    # Read input from standard input
    n = int(input())
    A = input().strip()
    m = int(input())
    B = input().strip()

    # Initialize dp table with size (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                # If characters match, calculate similarity score
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 4
            else:
                # If characters don't match, calculate similarity score
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The maximum similarity score is stored in dp[n][m]
    print(dp[n][m])
