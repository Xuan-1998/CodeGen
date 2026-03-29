import sys

def solve():
    t = int(input())
    MOD = 10**8 + 7
    dp = [[[0] * (5*10**5+1) for _ in range(10**5+1)] for _ in range(10**5+1)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == m:
                dp[i][j] = 1
            elif i == n-1 and j == m-1:
                dp[i][j] = 1
            else:
                k = min(max(i, n-i), 2*i)
                for p in range(k+1):
                    if 2*p <= n:
                        dp[i][j] += dp[p][m-j-1]
                    else:
                        dp[i][j] += 1

    print(*[sum(dp[n-1][i]) % MOD for i in range(m)], sep='\n')

solve()
