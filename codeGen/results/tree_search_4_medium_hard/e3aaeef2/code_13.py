import sys

def solve():
    t = int(input())
    
    MOD = 10**9 + 7
    
    dp = [[0, 1] for _ in range(100010)]
    
    for i in range(len(dp)):
        for j in range(2):
            if i == 0:
                continue
            dp[i][j] = (dp[i-1][j^1] + 1) % MOD

    for _ in range(t):
        n, m = map(int, input().split())
        
        print((dp[n%MOD][m%2]) % MOD)

if __name__ == "__main__":
    solve()
