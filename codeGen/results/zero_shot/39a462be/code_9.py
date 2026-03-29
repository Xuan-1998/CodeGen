import sys

def find_lcs(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

def compute_similarity_score(A, B):
    lcs_length = find_lcs(A, B)
    a_len, b_len = len(A), len(B)
    similarity_score = 4 * lcs_length - (a_len + b_len)
    return max(similarity_score)

A = input().strip()
B = input().strip()

similarity_score = compute_similarity_score(A, B)
print(similarity_score)
