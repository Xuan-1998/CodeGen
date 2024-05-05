import sys

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

def calculate_similarity(A, B):
    lcs_len = lcs_length(A, B)
    similarity_score = 4 * lcs_len - (len(A) + len(B))
    return similarity_score

A = input().strip()
B = input().strip()

max_similarity = 0
for i in range(len(A)):
    for j in range(i + 1):
        substring_A = A[j:i+1]
        for k in range(len(B)):
            for l in range(k + 1):
                substring_B = B[l:k+1]
                similarity_score = calculate_similarity(substring_A, substring_B)
                max_similarity = max(max_similarity, similarity_score)

print(max_similarity)
