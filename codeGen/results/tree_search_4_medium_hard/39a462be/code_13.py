from collections import defaultdict

def maximal_similarity_score():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the base case
    for i in range(n + 1):
        dp[i][0] = -i
    for j in range(m + 1):
        dp[0][j] = -j

    # Fill up the DP table
    memo = defaultdict(int)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 4
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximal similarity score over all pairs of substrings
    max_similarity_score = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                max_similarity_score = max(max_similarity_score, dp[i][j])

    return max_similarity_score

print(maximal_similarity_score())
