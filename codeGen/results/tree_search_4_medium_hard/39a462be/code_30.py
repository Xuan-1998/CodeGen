from bisect import bisect_left
from collections import defaultdict

def similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize the base case: when both strings are empty, the similarity score is 0.
    dp[0][0] = 0
    
    # Create a dictionary to store the length of substrings
    substrings = defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            # Find the LCS of A[i..n) and B[j..m)
            lcs_len = bisect_left(substrings, len(A[i:])) - 1
            if lcs_len >= 0:
                dp[i][j] = max(dp[i-1][j-1] + 4 * lcs_len, dp[i-1][j] + dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n-1][m-1]
