def similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: when either i or j reaches the end of one of the strings
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the final similarity score
    lcs_length = dp[n][m]
    return 4 * lcs_length - (n + m)

# Read input from stdin
A = input().strip()
B = input().strip()

# Print the answer to stdout
print(similarity_score(A, B))
