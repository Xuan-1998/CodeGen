python
# Step 1: Read input strings A and B from stdin
A = input().strip()
B = input().strip()

# Step 2: Initialize a 2D array to store lengths of LCS for substrings
n, m = len(A), len(B)
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Step 3: Fill the dp array using dynamic programming
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# Step 4: Calculate the similarity score for each pair of substrings
max_similarity = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(m):
            for l in range(k + 1, m):
                # Calculate the LCS length for this pair of substrings
                lcs_length = dp[j][l]
                # Calculate the similarity score for this pair of substrings
                similarity = 4 * lcs_length - (j - i + 1) - (l - k + 1)
                max_similarity = max(max_similarity, similarity)

# Step 5: Print the maximum similarity score to stdout
print(max_similarity)
