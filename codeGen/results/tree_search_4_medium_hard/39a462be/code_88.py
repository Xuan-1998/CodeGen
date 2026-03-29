def similarity_score(A, B):
    n = len(A)
    m = len(B)

    # Initialize the 2D table to store the LCS scores
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: when one or both strings are empty, the LCS is an empty string
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Fill up the table using dynamic programming with memoization
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 4 * (dp[i - 1][j - 1] + 1) - i - j
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the final similarity score
    return max(max(row) for row in dp)

# Read input strings from stdin and calculate the similarity score
A = input().strip()
B = input().strip()

print(similarity_score(A, B))
