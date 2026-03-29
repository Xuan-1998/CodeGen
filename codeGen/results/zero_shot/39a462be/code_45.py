import sys

def lcs_length(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

def max_similarity_score(A, B):
    n = len(A)
    m = len(B)

    max_score = 0

    for i in range(n):
        for j in range(m):
            k = min(i + 1, n) - 1
            l = min(j + 1, m) - 1
            lcs_len = lcs_length(A[i:k+1], B[j:l+1])
            score = 4 * lcs_len - (k + 1) - (l + 1)
            max_score = max(max_score, score)

    return max_score

A = input().strip()
B = input().strip()

print(max_similarity_score(A, B))
