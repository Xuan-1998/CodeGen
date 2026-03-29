def lcs_length(substr1, substr2):
    m, n = len(substr1), len(substr2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if substr1[i - 1] == substr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def similarity_score(substr1, substr2):
    lcs_length_val = lcs_length(substr1, substr2)
    return 4 * lcs_length_val - (len(substr1) + len(substr2))

A = input().strip()
B = input().strip()

max_similarity_score = 0
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        substr1 = A[i:j]
        for k in range(len(B)):
            for end in range(k + 1, len(B) + 1):
                substr2 = B[k:end]
                max_similarity_score = max(max_similarity_score, similarity_score(substr1, substr2))

print(max_similarity_score)
