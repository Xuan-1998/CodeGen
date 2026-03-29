def lcs(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(A, B):
    lcs_len = lcs(A, B)
    return 4 * lcs_len - (len(A) + len(B))

def max_similarity_score(A, B):
    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for end in range(k + 1, len(B) + 1):
                    subscore = similarity_score(A[i:j], B[k:end])
                    max_score = max(max_score, subscore)

    return max_score

# Read input strings from stdin
A = input().strip()
B = input().strip()

# Calculate and print the maximal similarity score
max_score = max_similarity_score(A, B)
print(max_score)
