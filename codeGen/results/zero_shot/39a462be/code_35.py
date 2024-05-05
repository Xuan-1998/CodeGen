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

def similarity_score(a, b):
    lcs_length_val = lcs_length(a, b)
    return 4 * lcs_length_val - (len(a) + len(b))

a = input().strip()
b = input().strip()

print(similarity_score(a, b))
