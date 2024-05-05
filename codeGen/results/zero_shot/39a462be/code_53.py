# Step 1: Define the function to calculate LCS
def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Step 2: Calculate the similarity score for each pair of substrings
def calculate_similarity(A, B):
    n = len(A)
    m = len(B)

    similarity_score = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calculate the LCS of substring A[i..] and substring B[j..]
            lcs_length = longest_common_subsequence(A[i - 1:], B[j - 1:])
            
            # Calculate the similarity score
            similarity_score += 4 * lcs_length - (i + j)

    return similarity_score

# Step 3: Read input from stdin and print output to stdout
A = input().strip()
B = input().strip()

similarity_score = calculate_similarity(A, B)
print(similarity_score)
