from sys import stdin, stdout
from collections import deque

def calculate_similarity_score(A, B):
    n = len(A)
    m = len(B)
    
    dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if not A or not B:
                dp[i][j][0] = 0
            else:
                k = min(i, j)
                while k >= 0 and (A[:i-k] == B[:j-k]):
                    k -= 1
                dp[i][j][0] = max(dp[i-1][j-1][0], dp[i-1][j][0], dp[i][j-1][0]) + (4 * (k+1) - i - j)
    
    return dp[n][m][0]

A, B = stdin.readline().split()
n, m = map(int, A.split())
A, B = A[:n], B[:m]
stdout.write(str(calculate_similarity_score(A, B)) + '\n')
