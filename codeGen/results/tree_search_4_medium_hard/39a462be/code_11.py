def lcs_length(A, B):
    m = len(A)
    n = len(B)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A, B):
    m = len(A)
    n = len(B)

    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j][0] = dp[i - 1][j - 1][0] + (4 * lcs_length(A[:i], B[:j]) - (i + j))
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])

    return max([max(row) for row in dp])

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
