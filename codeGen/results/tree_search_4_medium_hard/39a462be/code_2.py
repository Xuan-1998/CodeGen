import sys

def lcs_length(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def maximal_similarity_score(A, B):
    m, n = len(A), len(B)
    score_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            lcs_length_score = 4 * lcs_length(A[i - m:i], B[j - n:j])
            score_table[i][j] = max(score_table[i - 1][j], score_table[i][j - 1]) - lcs_length_score

    return max(max(row) for row in score_table)

A, B = [input().strip() for _ in range(2)]
print(maximal_similarity_score(A, B))
