from math import gcd

def min_squares(n, m):
    dp = {(i, j): float('inf') for i in range(n+1) for j in range(m+1)}
    
    def solve(i, j):
        if i == 0 and j == 0: return 0
        if i > 0 and j > 0:
            side_len = gcd(i, j)
            dp[i][j] = min(dp[max(0, i-side_len)][max(0, j-side_len)],
                           dp[max(0, i-side_len)][j], 
                           dp[i][max(0, j-side_len)]) + 1
        return dp[i][j]
    
    return solve(n, m)

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
