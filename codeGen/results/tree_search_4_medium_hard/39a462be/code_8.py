def max_similarity_score():
    A = input().strip()
    B = input().strip()

    n = len(A)
    m = len(B)

    # Create a suffix tree for each string
    SA = []
    SB = []

    for i in range(n):
        SA.append(A[i:])

    for j in range(m):
        SB.append(B[j:])

    # Initialize the DP table with base cases
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    # Fill the DP table using the suffix tree
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if SA[i - 1] == SB[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 4
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximum similarity score
    max_score = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if SA[i] == SB[j]:
                max_score = max(max_score, dp[i][j] - (i + j))

    return max_score

print(max_similarity_score())
