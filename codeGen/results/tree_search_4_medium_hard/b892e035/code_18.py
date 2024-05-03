import math
import sys

def solve():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        dp = [[0.0] * 17 for _ in range(n+1)]
        dp[0][8] = 1
        
        for i in range(1, n+1):
            a, b, p1, p2 = map(float, sys.stdin.readline().split())
            
            for j in range(16+1):
                if dp[i-1][j] > 0:
                    dp[i][min(j+a, 16)] += dp[i-1][j] * (1-p1)
                    dp[i][max(0, j-b)] += dp[i-1][j] * p2
        print(math.floor(sum(dp[n][i] for i in range(17)) * 100000) / 100000)

if __name__ == "__main__":
    solve()
