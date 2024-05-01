from sys import stdin, max
read = lambda: map(int, stdin.readline().split())

n, m = read()
dp = [[0] * (m+1) for _ in range(n+1)]

def solve(i, j):
    if i == 0 or j == 0:
        return 0
    min_squares = float('inf')
    
    for k in range(1, min(i, j)+1):
        square_size = k*k
        remaining_i = i - k
        remaining_j = j - k
        if (remaining_i > 0 and remaining_j > 0) or (k == 1):
            dp[i][j] = min(dp[i][j], solve(remaining_i, remaining_j) + 1)
    return dp[i][j]

print(solve(n, m))
