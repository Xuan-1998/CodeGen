def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(m):
                if j % 2 == 0:
                    # even index, can place any of the n letters
                    dp[i][j + 1] += dp[i][j] * n
                else:
                    # odd index, last letter must be from position i in the alphabet
                    dp[i][j + 1] += dp[i - 1][j] * (n - i + 1)
            dp[i][m] = (dp[i][m - 1] + n) % (10**8 + 7)

        print(dp[1][m])
