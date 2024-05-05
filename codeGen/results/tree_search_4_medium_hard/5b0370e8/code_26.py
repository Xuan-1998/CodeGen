import sys

def solve():
    t = int(sys.stdin.readline())
    MOD = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        # base case: when i = 0
        for j in range(k+1):
            if not (j & (j-1)):  # if j is a power of 2
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        
        for i in range(1, n+1):
            for j in range(k+1):
                if j & (j-1):  # if j is not a power of 2
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
        
        ans = dp[n][k]
        
        print(ans)

if __name__ == '__main__':
    solve()
