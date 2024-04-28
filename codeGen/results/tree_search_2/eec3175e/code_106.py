code
import sys

def solve():
    n, m = map(int, input().split())
    dp = [[False] * (n+1) for _ in range(m+1)]
    
    for j in range(m+1):
        dp[j][0] = True
    
    for i in range(n+1):
        for j in range(1, m+1):
            if i == 0:
                dp[j][i] = (j % m) == 0
            else:
                dp[j][i] = any(dp[(k % m)][x-1] for x in range(i+1))

    print(int(any(dp[j][n] for j in range(m+1))))

solve()
