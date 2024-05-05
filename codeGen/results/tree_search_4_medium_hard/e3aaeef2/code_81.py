def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(10)]
        for i in range(10):
            dp[i][0] = 1
        for j in range(1, m + 1):
            for i in range(10):
                if j > 0:
                    dp[(i + 1) % 10][j - 1] += dp[i][j]
        print((dp[9][m] - (n // 10 ** (m + 1)) * (10 ** m)) % (10 ** 9 + 7))

solve()
