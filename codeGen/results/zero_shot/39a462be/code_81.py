def lcs_length(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def max_similarity_score(a, b):
    m, n = len(a), len(b)
    max_score = 0
    
    for i in range(m):
        for j in range(i + 1, m + 1):
            for k in range(n):
                for end in range(k + 1, n + 1):
                    score = 4 * lcs_length(a[i:j], b[k:end]) - (j - i) - (end - k)
                    max_score = max(max_score, score)
    
    return max_score

import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

print(max_similarity_score(a, b))
