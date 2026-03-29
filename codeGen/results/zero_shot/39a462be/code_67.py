# Python script for maximal similarity score
from sys import stdin, stdout

# Read input strings A and B
A = stdin.readline().strip()
B = stdin.readline().strip()

# Initialize dynamic programming table
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

# Fill the dynamic programming table
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# Calculate the maximal similarity score
max_similarity_score = 4 * dp[-1][-1] - (len(A) + len(B))

# Print the result
stdout.write(str(max_similarity_score) + '\n')
