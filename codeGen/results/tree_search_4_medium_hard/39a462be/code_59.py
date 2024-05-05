import sys

def lcs_length(A, B, i, j):
    dp = [[0] * (j + 1) for _ in range(i + 1)]
    for x in range(i + 1):
        for y in range(j + 1):
            if x == 0:
                dp[x][y] = y
            elif y == 0:
                dp[x][y] = x
            elif A[x - 1] == B[y - 1]:
                dp[x][y] = 1 + dp[x - 1][y - 1]
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
    return dp[i][j]

def similarity_score(A, B):
    max_similarity = float('-inf')
    for i in range(len(A)):
        for j in range(len(B)):
            k = lcs_length(A[i:], B[j:], len(A) - i, len(B) - j)
            score = 4 * k - (len(A) + len(B))
            max_similarity = max(max_similarity, score)
    return max_similarity

A, B = input().split()
n, m = len(A), len(B)
print(similarity_score(A, B))
