import sys

def read_input():
    A = input().strip()
    B = input().strip()
    return A, B

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
    lcs_len = lcs_length(A, B)
    A_len, B_len = len(A), len(B)
    return 4 * lcs_len - (A_len + B_len)

A, B = read_input()
print(similarity_score(A, B))
