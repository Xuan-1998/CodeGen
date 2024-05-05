import sys

def lcs_length(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A, B):
    m = len(A)
    n = len(B)
    lcs_len = lcs_length(A, B)
    return 4 * lcs_len - (m + n)

A = input().strip()
B = input().strip()
max_similarity_score = 0

for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for end in range(k + 1, len(B) + 1):
                substr_A = A[i:j]
                substr_B = B[k:end]
                similarity_score_local = similarity_score(substr_A, substr_B)
                max_similarity_score = max(max_similarity_score, similarity_score_local)

print(max_similarity_score)
