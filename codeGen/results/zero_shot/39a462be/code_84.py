import sys
from io import StringIO, BytesIO

def read_input():
    A = input().strip()
    B = input().strip()
    return A, B

A, B = read_input()

def get_lcs(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    
    return dp[m][n]

def get_similarity_score(A, B):
    lcs_length = get_lcs(A, B)
    return (4 * lcs_length) - (len(A) + len(B))

print(get_similarity_score(A, B))
