import math

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[0.0] * 17 for _ in range(n + 1)]
        dp[n][0] = 1.0
        for i in range(n - 1, -1, -1):
            p = [1.0] * 16
            for j in range(2):
                for k in range(16):
                    if (k & (1 << j)) == 0:
                        dp[i][j] += dp[i + 1][k] * p[k]
            p[0] = 0.0
        print(math.floor(dp[0][0]))

solve()
