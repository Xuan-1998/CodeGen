from functools import lru_cache

@lru_cache(None)
def lcs_length(i, j):
    if i == 0 or j == 0:
        return 0
    if A[i-1] == B[j-1]:
        return 1 + lcs_length(i-1, j-1)
    else:
        return max(lcs_length(i-1, j), lcs_length(i, j-1))

def dp_solution():
    global dp
    for i in range(m+1):
        for j in range(n+1):
            if i > 0 and j > 0:
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 4
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = 0
    return dp[m][n]

A, B = input().split()
m, n = len(A), len(B)
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

print(dp_solution())
