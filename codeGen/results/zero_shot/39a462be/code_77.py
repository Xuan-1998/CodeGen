def lcs_length(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def similarity_score(s1, s2):
    lcs_len = lcs_length(s1, s2)
    return 4 * lcs_len - len(s1) - len(s2)

a = input().strip()
b = input().strip()

max_similarity = 0

for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        for k in range(len(b)):
            for end in range(k + 1, len(b) + 1):
                substr_a = a[i:j]
                substr_b = b[k:end]
                max_similarity = max(max_similarity, similarity_score(substr_a, substr_b))

print(max_similarity)
