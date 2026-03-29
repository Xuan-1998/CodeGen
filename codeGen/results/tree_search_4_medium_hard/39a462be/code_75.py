def max_similarity_score(A, B):
    n = len(A)
    m = len(B)

    # Create a 3D table to store the lengths of common subsequences.
    dp = [[[0] * (min(n+1, m+1)) for _ in range(m+1)] for _ in range(n+1)]

    # Initialize the base case: when there are no more characters to compare.
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = [0]

    # Fill up the table using dynamic programming.
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + [dp[i-1][j-1][-1]+1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Calculate the maximum similarity score.
    k = dp[n][m][-1]
    return 4*k - n - m
