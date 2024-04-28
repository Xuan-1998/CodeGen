import sys

def solve():
    k = 10**5
    MOD = 10**9 + 7
    
    a, b = map(int, input().split())
    
    dp = [[0] * (k+1) for _ in range(k+1)]
    
    for i in range(k):
        for j in range(min(i, k-1), -1, -1):
            if i >= 2:
                dp[i][j+1] += dp[i-1][j]
            elif a & (1 << i):
                dp[i][j+1] = dp[i][j+1] | 1
            else:
                dp[i][j+1] = 0
            
            if j < k - 1:
                dp[i][j+1] += dp[i-1][k-1]
            
            dp[i][j+1] %= MOD
    
    print(sum(dp[k][i] for i in range(k+1)) % MOD)

if __name__ == "__main__":
    solve()
