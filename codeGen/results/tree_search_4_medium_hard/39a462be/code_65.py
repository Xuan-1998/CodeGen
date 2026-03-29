def lcs_similarity(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the base case
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximum similarity score
    lcs_length = dp[n][m]
    total_length = n + m
    return 4 * lcs_length - total_length

# Read input strings from standard input
A = input().strip()
B = input().strip()

# Calculate and print the maximum similarity score
print(lcs_similarity(A, B))
