def max_similarity_score():
    A, B = [input().strip() for _ in range(2)]
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            k = min(i, j)
            while A[i - k:i] != B[j - k:j]:
                k -= 1
            dp[i][j] = max(dp[i - k][j - k] + 4 * k, i + j)

    return dp[n][m]

print(max_similarity_score())
