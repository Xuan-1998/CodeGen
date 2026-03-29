def lcs(A, B):
    m = len(A)
    n = len(B)

    # Create a 2D array to store the lengths of common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0

    # Fill up the dp array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the similarity score based on the LCS length
    return 4 * max_length - m - n + 4

A = input().strip()
B = input().strip()

print(lcs(A, B))
