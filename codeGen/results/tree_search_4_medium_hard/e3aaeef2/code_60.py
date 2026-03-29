def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(10)]

        for i in range(1, 10):
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = 1
                elif j > 0:
                    dp[i][j] = (dp[i-1][j-1] + 1) % (10**9 + 7)

        res = 0
        while n:
            last_digit = n % 10
            if last_digit == 9:
                res += m + 1
            else:
                res += dp[last_digit][m]
            n //= 10

        print(res)
