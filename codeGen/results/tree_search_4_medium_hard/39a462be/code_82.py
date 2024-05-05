def lcs_length(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

def maximal_similarity_score(A, B):
    n, m = len(A), len(B)
    lcs_length_value = lcs_length(A, B)
    
    return 4 * lcs_length_value - (n + m)

# Test case
A = input().strip()
B = input().strip()

print(maximal_similarity_score(A, B))
