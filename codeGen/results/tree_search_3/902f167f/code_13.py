import sys

def min_squares(n, m):
    if n < 1 or m < 1:
        return float('inf')
    if n == 0 or m == 0:
        return 0
    
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i * j == 0:
            return 0
        
        min_tiles = float('inf')
        
        for k in range(1, i + 1):
            for l in range(1, j + 1):
                if k * l <= i and k * l <= j:
                    min_tiles = min(min_tiles, dp(i - k, j) + dp(i, j - k) + 1)
        
        memo[(i, j)] = min_tiles
        return min_tiles
    
    return dp(n - 1, m - 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    if 1 <= n <= 13 and 1 <= m <= 13:
        print(min_squares(n, m))
    else:
        sys.exit(0)
