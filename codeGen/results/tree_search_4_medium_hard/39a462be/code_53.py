from collections import deque

def max_similarity_score(A, B):
    dp = [[[0 for _ in range(max(len(A), len(B)) + 1)] for _ in range(max(len(A), len(B)) + 1)] for _ in range(max(len(A), len(B)) + 1)]

    for i in range(1, max(len(A), len(B)) + 1):
        for j in range(1, max(len(A), len(B)) + 1):
            for k in range(max(len(A), len(B)) + 1):
                if k == 0:
                    dp[i][j][k] = 4 * min(i, j) - (i + j)
                else:
                    if A[i-1] == B[j-1]:
                        dp[i][j][k] = max(dp[i-1][j-1][k-1], 4*k-(i+j))
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k])

    return max([max(row) for row in dp[-1]])

# Read input from stdin
A, B = [line.strip() for line in sys.stdin]

# Calculate and print the maximum similarity score
print(max_similarity_score(A, B))
