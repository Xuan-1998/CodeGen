def get_similarity_score(A, B):
    n = len(A)
    m = len(B)

    # Create a 2D array to store lengths of LCS
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the 2D array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the similarity score using the filled 2D array
    lcs_length = dp[n][m]
    return 4 * lcs_length - (n + m)

# Read input from stdin
A = input().strip()
B = input().strip()

# Calculate and print the maximal similarity score
print(get_similarity_score(A, B))
