import sys

def lcs_length(substring1, substring2):
    m = len(substring1)
    n = len(substring2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif substring1[i - 1] == substring2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def similarity_score(substring1, substring2):
    lcs_length_val = lcs_length(substring1, substring2)
    return 4 * lcs_length_val - len(substring1) - len(substring2)

def max_similarity_score(A, B):
    max_similarity = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            substring1 = A[i:j]
            for k in range(len(B)):
                for end in range(k + 1, len(B) + 1):
                    substring2 = B[k:end]
                    max_similarity = max(max_similarity, similarity_score(substring1, substring2))
    
    return max_similarity

A = input().strip()
B = input().strip()

print(max_similarity_score(A, B))
