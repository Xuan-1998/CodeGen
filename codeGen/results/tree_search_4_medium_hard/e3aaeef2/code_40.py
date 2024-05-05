def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        MOD = 10**9 + 7
        dp = [[0] * (m+1) for _ in range(11)]
        dp[1][0] = 1

        for i in range(2, 11):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    last_digit = n // 10**(i-1) % 10
                    if (last_digit + 1) * 10**(i-1) <= n:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1])
                    else:
                        dp[i][j] = dp[i-1][j]
                n %= 10**i
        print((dp[10][m]) % MOD)
