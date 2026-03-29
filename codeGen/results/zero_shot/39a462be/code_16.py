def lcs_length(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

max_similarity_score = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        lcs_length_ij = lcs_length(A[:i], B[:j])
        similarity_score_ij = 4 * lcs_length_ij - (i + j)
        max_similarity_score = max(max_similarity_score, similarity_score_ij)

print(max_similarity_score)
