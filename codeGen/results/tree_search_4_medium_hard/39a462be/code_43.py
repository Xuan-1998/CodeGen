import os

def similarity_score(A, B):
    # Initialize dp with size (n+1) x (m+1), where n and m are the lengths of strings A and B respectively.
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill up the first row and column with values based on the length of strings A and B.
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Iterate over each character in both strings, and update the dynamic programming table accordingly.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                # If characters match, recursively call the function with reduced lengths (i-1) and (j-1), and increment k.
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Else, set k to 0 and move on.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximum similarity score based on the length of the longest common subsequence and the total lengths of strings A and B.
    return 4 * (n + m - 2 * dp[n][m]) - (n + m)

# Read input from standard input
A = input().strip()
B = input().strip()

# Print the output to standard output
print(similarity_score(A, B))
