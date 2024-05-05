import sys

def lcs_length(A, B):
    m, n = len(A), len(B)
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
    m, n = len(A), len(B)
    lcs_len = lcs_length(A, B)
    score = 4 * lcs_len - (m + n)

    return score

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
