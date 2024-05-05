import sys

def lcs_length(A, B):
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

def similarity_score(A, B):
    n, m = len(A), len(B)
    lcs_length_A_B = lcs_length(A + '#' + B[::-1], '#' + '#')
    return 4 * lcs_length_A_B - (n + m)

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
