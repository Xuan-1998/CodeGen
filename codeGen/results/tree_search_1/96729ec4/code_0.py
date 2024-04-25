import sys

def count_square_submatrices(A, N, M):
    dp = [[0] * M for _ in range(N)]
    total = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                total += dp[i][j]

    return total

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
A = [sys.stdin.readline().strip() for _ in range(N)]

# Count the number of square submatrices and print the result to stdout
result = count_square_submatrices(A, N, M)
print(result)
