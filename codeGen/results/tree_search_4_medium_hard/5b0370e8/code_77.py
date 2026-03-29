import sys

def solve():
    t = int(input())
    MOD = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        dp = [[[0] * (k+1) for _ in range(2**k)] for _ in range(n+1)]
        
        dp[0][0][0] = 1
        
        for i in range(1, n+1):
            for j in range(2**k):
                for l in range(k, -1, -1):
                    if (j >> l) & 1:
                        dp[i][j][l] = (dp[i-1][(j^(1<<l))]%MOD + dp[i-1][j]%MOD) % MOD
                    else:
                        dp[i][j][l] = dp[i-1][j]%MOD
        
        ans = sum(dp[n][2**k-1])
        
        print(ans%MOD)

if __name__ == "__main__":
    solve()
