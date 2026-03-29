def find_max_similarity_score(A, B):
    # Initialize maximum similarity score
    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for end in range(k + 1, len(B) + 1):
                    # Calculate the length of LCS
                    lcs_length = find_LCS_length(A[i:j], B[k:end])

                    # Calculate the similarity score
                    score = 4 * lcs_length - (j - i) - (end - k)

                    # Update maximum similarity score if necessary
                    max_score = max(max_score, score)

    return max_score

def find_LCS_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Receive input from stdin
A = input().strip()
B = input().strip()

# Calculate and print the maximum similarity score
print(find_max_similarity_score(A, B))
