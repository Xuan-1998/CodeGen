code
import sys

n = int(input().strip())
m = int(input().strip())

dp = [[[-1 for _ in range(m+1)] for _ in range(n+1)]]  # Initialize table with all elements set to -1

for i in range(1, n+1):
    for j in range(1, m+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 4
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # Calculate the base case when one or both strings are empty
        if i == 0 or j == 0:
            dp[i][j] = n + m - 4 * min(i, j)

max_similarity_score = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        similarity_score = dp[i][j]
        # Check if this substring pair has a higher similarity score than the current maximum
        max_similarity_score = max(max_similarity_score, similarity_score)

print(max_similarity_score)
code
