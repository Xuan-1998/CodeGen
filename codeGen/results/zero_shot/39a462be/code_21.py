def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
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

def calculate_similarity_score(s1, s2):
    lcs_length_value = lcs_length(s1, s2)
    similarity_score = 4 * lcs_length_value - (len(s1) + len(s2))
    return similarity_score

A = input().strip()
B = input().strip()

max_similarity_score = 0
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for end_k in range(k + 1, len(B) + 1):
                s1 = A[i:j]
                s2 = B[k:end_k]
                max_similarity_score = max(max_similarity_score, calculate_similarity_score(s1, s2))

print(max_similarity_score)
