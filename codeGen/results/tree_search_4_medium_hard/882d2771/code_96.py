import sys

def solve():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7
    
    dp = [[0] * (r+1) for _ in range(t+1)]
    
    for i in range(t+1):
        dp[i][1] = 1
    for j in range(2, r+1):
        dp[0][j] = j - 1
    
    for i in range(1, t+1):
        for j in range(l, r+1):
            dp[i][j] = min(dp[i-1][k] + (j-k) for k in range(l, j+1)) % MOD
    
    print(dp[t][r])

if __name__ == "__main__":
    solve()
