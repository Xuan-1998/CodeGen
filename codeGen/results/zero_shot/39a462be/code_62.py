def lcs_length(substring_a, substring_b):
    m = len(substring_a)
    n = len(substring_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif substring_a[i - 1] == substring_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def similarity_score(substring_a, substring_b):
    lcs_length_result = lcs_length(substring_a, substring_b)
    return 4 * lcs_length_result - (len(substring_a) + len(substring_b))

def maximal_similarity_score(A, B):
    max_score = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            substring_a = A[i:j]
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    substring_b = B[k:l]
                    score = similarity_score(substring_a, substring_b)
                    if score > max_score:
                        max_score = score
    return max_score

A = input().strip()
B = input().strip()

print(maximal_similarity_score(A, B))
