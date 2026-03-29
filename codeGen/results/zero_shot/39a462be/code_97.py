import sys

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def calculate_similarity_score(A, B):
    lcs_length_ab = lcs_length(A + '#' + B[::-1], '#' + '#')
    return 4 * lcs_length_ab - (len(A) + len(B))

A = input().strip()
B = input().strip()

print(calculate_similarity_score(A, B))
