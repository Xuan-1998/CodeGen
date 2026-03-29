code = """
import sys
n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

max_sim = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        lcs_length = dp[i][j]
        similarity_score = 4*lcs_length - (i + j)
        max_sim = max(max_sim, similarity_score)

print(max_sim)
"""

