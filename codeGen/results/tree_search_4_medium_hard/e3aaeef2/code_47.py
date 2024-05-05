import sys
mod = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            if i < 10:
                dp[i][0] = 1
            else:
                dp[i][0] = i
        
        s = set()
        for j in range(m + 1):
            for i in range(n + 1):
                if i not in s:
                    if i < 10:
                        dp[i][j+1] = 1
                    else:
                        dp[i][j+1] = min(10 * (i-1) + 2, mod)
                    for k in range(i - 1, 0, -1):
                        if k not in s:
                            dp[k][j+1] += dp[i-1][j] * (k+1)
                            dp[k][j+1] %= mod
                dp[i][j+1] += dp[i-1][j]
                dp[i][j+1] %= mod
            s.add(i)
        
        print(dp[n][m] % mod)

solve()
