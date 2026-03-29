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

def similarity_score(A, B):
    total_length = len(A) + len(B)
    max_similarity = 0

    for i in range(len(A)):
        for j in range(len(B)):
            lcs_len = lcs_length(A[i:], B[j:])
            similarity = 4 * lcs_len - total_length
            max_similarity = max(max_similarity, similarity)

    return max_similarity

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
