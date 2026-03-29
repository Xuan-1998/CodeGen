def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(11)]
        for i in range(1, 11):
            dp[i][0] = i
        for j in range(m + 1):
            for k in range(min(j // 10 + 1, 10)):
                dp[k][j] = max(dp[k][j], dp[min(k + 1, 10)][j - k * 10] + 1)
        print((dp[0][m] + 1) % (10**9 + 7))

solve()
