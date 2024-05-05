import sys

n, m = map(int, input().split())
A = input()
B = input()

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

max_similarity = 0
for i in range(n+1):
    for j in range(m+1):
        similarity = 4 * dp[i][j] - (i + j)
        max_similarity = max(max_similarity, similarity)

print(max_similarity)
