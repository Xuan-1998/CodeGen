def solve():
    t = int(input())
    for _ in range(t):
        n, m, c = map(int, input().split())
        u = list(map(int, input().split()))
        l = list(map(int, input().split()))

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if u[i - 1] >= l[j - 1]:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10 ** 9 + 7)
                else:
                    dp[i][j] = dp[i - 1][j]
            for j in range(m, -1, -1):
                if u[i - 1] >= l[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % (10 ** 9 + 7)
                else:
                    break

        print(*dp[n], sep=' ')
