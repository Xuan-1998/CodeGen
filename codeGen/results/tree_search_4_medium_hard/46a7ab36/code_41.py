from math import ceil

def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        MOD = 10**8 + 7
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = 1
        
        for j in range(1, m+1):
            for i in range(1, min(n-1, 2*j)+1):
                if 2*i <= n or j == 1:
                    dp[i][j] = sum(dp[k][j-1] % MOD for k in range(max(0, i-n), min(i+1, n))) * (i<ceil(n/2) or j>1)
                else:
                    dp[i][j] = dp[2*i%MOD][j-1]
        
        print(dp[n][m]%MOD)

if __name__ == "__main__":
    solve()
