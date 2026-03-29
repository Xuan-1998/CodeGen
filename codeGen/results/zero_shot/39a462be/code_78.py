import sys

def lcs_length(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def calculate_similarity_score(a, b):
    lcs_len = lcs_length(a, b)
    similarity_score = 4 * lcs_len - (len(a) + len(b))
    return similarity_score

a = input().strip()
b = input().strip()

max_similarity_score = 0
for i in range(len(a)):
    for j in range(i + 1):
        for k in range(len(b)):
            for t in range(k + 1):
                substring_a = a[j:i+1]
                substring_b = b[t:k+1]
                similarity_score = calculate_similarity_score(substring_a, substring_b)
                max_similarity_score = max(max_similarity_score, similarity_score)

print(max_similarity_score)
