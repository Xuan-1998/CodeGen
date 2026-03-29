from sys import stdin

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
    score = 0
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and j > 0:
                lcs_len = lcs_length(A[:i], B[:j])
                score += 4 * lcs_len - (i + j)
    
    return score

A, B = [line.strip() for line in stdin.readlines()]
print(similarity_score(A[0], B[0]))
