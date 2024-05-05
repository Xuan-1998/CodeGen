from io import StringIO
import sys

def read_input():
    A, B = map(StringIO, sys.stdin.readline().strip().split())
    return [line.strip() for line in A], [line.strip() for line in B]

def similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(2):
        for k in range(m + 1):
            if i == 0:
                for j in range(n + 1):
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j-1][k], dp[i][j][k-1])
                    else:
                        dp[i][j][k] = k
            else:
                for j in range(n + 1):
                    if j > 0 and k > 0:
                        if A[j-1] == B[k-1]:
                            dp[i][j][k] = dp[i][j-1][k-1] + 1
                        else:
                            dp[i][j][k] = max(dp[i][j-1][k], dp[i][j][k-1])
                    elif j > 0:
                        dp[i][j][k] = max(dp[i][j-1][k], dp[i][j][k-1])
                    else:
                        dp[i][j][k] = k

    return dp[1][n][m]

A, B = read_input()
print(similarity_score(A, B))
