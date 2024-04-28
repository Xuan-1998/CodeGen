import sys

n, m = map(int, input().split())

dp = [[0]*(m+1) for _ in range(n+1)]

def f(i, j):
    if i == 1 or j == 1:
        return max(i, j)
    if dp[i][j] > 0:
        return dp[i][j]
    min_squares = float('inf')
    if i > 1:
        min_squares = min(min_squares, f(i-1, j) + 1)
    if j > 1:
        min_squares = min(min_squares, f(i, j-1) + 1)
    dp[i][j] = min_squares
    return min_squares

print(f(n, m))
