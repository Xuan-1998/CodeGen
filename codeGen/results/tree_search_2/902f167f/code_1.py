from collections import defaultdict

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Base case: a rectangle of size 0 x m or n x 0 can be tiled with 0 squares
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    memo = defaultdict(int)
    
    def solve(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i * j == 0:
            return 0
        
        min_squares = float('inf')
        for k in range(1, min(i, j) + 1):
            # Try to tile the rectangle with a square of size k x k
            squares = solve(i - k, j - k) + (i // k + j // k)
            if squares < min_squares:
                min_squares = squares
        
        memo[(i, j)] = min_squares
        return min_squares
    
    print(solve(n, m))

n, m = map(int, input().split())
min_squares(n, m)
