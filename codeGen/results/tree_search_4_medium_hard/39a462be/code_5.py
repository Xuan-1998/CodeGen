import sys
from collections import defaultdict

def lcs_length(A, B):
    m = len(A)
    n = len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def solve(A, B):
    m = len(A)
    n = len(B)
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            result = 0
        else:
            length_of_LCS = lcs_length(A[:i], B[:j])
            result = max(dp(i - 1, j - 1) + 4 * length_of_LCS, dp(i - 1, j), dp(i, j - 1))
        
        memo[(i, j)] = result
        return result
    
    return dp(m, n)

A = input().strip()
B = input().strip()

print(solve(A, B))
