def max_similarity(A, B):
    n = len(A)
    m = len(B)

    # Create a 2D table to store the LCS for all possible substrings
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the 2D table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the similarity score for all pairs of substrings
    max_similarity_score = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            lcs_length = dp[i][j]
            similarity_score = 4 * lcs_length - (i + j)
            max_similarity_score = max(max_similarity_score, similarity_score)

    return max_similarity_score

# Read input from standard input
A = input().strip()
B = input().strip()

# Calculate and print the maximum similarity score
print(max_similarity(A, B))
