import sys

def lcs_length(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def similarity_score(a, b):
    lcs_len = lcs_length(a, b)
    return 4 * lcs_len - (len(a) + len(b))

def max_similarity_score():
    A = input().strip()
    B = input().strip()
    max_score = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for end_k in range(k + 1, len(B) + 1):
                    score = similarity_score(A[i:j], B[k:end_k])
                    max_score = max(max_score, score)
    return max_score

print(max_similarity_score())
