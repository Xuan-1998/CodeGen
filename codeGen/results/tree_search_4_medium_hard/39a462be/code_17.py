from collections import defaultdict

A = input().strip()
B = input().strip()

m, n = len(A), len(B)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 4
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

max_similarity = max(dp[m][k] - k for k in range(n + 1)) + 4 * max(len(A) - m, len(B) - n)

print(max_similarity)
