import sys

sys.setrecursionlimit(1000000)

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(min(i, m)+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    if i % 2 == 0 and i//2 > n:
                        dp[i][j] = (dp[i//2][m-1] * (n - i//2) + dp[i][j-1] * min(i//2 + 1, n) - i//2)
                    else:
                        dp[i][j] = dp[i][j-1] * min(i//2 + 1, n) - i//2
        print((dp[n][m] + 7) % (10**8 + 7))

solve()
