import sys

def similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = max(4 * min(i, j) - i - j, 0)
            else:
                k = min(i, j)
                for l in range(k + 1):
                    dp[i][j] = max(dp[i-1][k-l] + dp[k-l][j-1] - l, dp[i][j])

    return dp[n][m]

A = input().strip()
B = input().strip()
print(similarity_score(A, B))
