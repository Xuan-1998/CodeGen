===BEGIN SOLUTION===
from itertools import zip_longest

def LCS(A, B):
    m = len(A)
    n = len(B)

    # Initialize the DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A, B):
    lcs_len = LCS(A, B)
    return 4 * lcs_len - (len(A) + len(B))

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
