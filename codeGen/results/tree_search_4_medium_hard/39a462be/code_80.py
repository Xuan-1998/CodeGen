def max_similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 4 * min(i, j) - i - j
            else:
                common_length = min(i, j)
                for k in range(common_length):
                    if A[i-1-k] == B[j-1-k]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 4 * common_length - i - j)
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return max(max(row) for row in dp)

# Receive input from stdin
A, B = input().split()
n, m = len(A), len(B)

# Calculate and print the maximum similarity score
print(max_similarity_score(A, B))
