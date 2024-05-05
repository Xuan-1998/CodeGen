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

def similarity_score(A, B):
    m, n = len(A), len(B)
    lcs_len = lcs_length(A, B)
    score = 4 * lcs_len - (m + n)
    return score

A = input().strip()
B = input().strip()

max_similarity = 0
for i in range(len(A)):
    for j in range(i + 1):
        for k in range(len(B)):
            for end in range(k + 1):
                lcs_len = lcs_length(A[j:i+1], B[k:end+1])
                score = similarity_score(A[j:i+1], B[k:end+1])
                max_similarity = max(max_similarity, score)

print(max_similarity)
