import sys

def solve(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                lcs_length = 1
                while i-lcs_length > 0 and j-lcs_length > 0:
                    if A[i-lcs_length-1] == B[j-lcs_length-1]:
                        lcs_length += 1
                    else:
                        break
                dp[i][j] = 4 * lcs_length + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return max(max(row) for row in dp)

# Read input from stdin
A = input().strip()
B = input().strip()

print(solve(A, B))
