def find_max_similarity_score():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_similarity_score = 0
    for i in range(n + 1):
        for j in range(m + 1):
            lcs_length = dp[i][j]
            similarity_score = 4 * lcs_length - (i + j)
            max_similarity_score = max(max_similarity_score, similarity_score)

    return max_similarity_score

print(find_max_similarity_score())
