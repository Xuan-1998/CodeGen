from collections import namedtuple

Row = namedtuple('Row', ['a', 'b', 'c'])

def solve():
    n = int(input())
    rows = [Row(*map(int, input().split()), *map(int, input().split()), *map(int, input().split())) for _ in range(n)]

    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(min(i, n)+1):
            if j == 0:
                dp[i][j] = max(dp[i-1][0], rows[i-1].a + (dp[i-2][0] if i > 1 else rows[i-1].b))
            else:
                dp[i][j] = max(dp[i-1][j], rows[i-1].c + dp[i-1][j-1])
    
    return dp[n][n]

print(solve())
