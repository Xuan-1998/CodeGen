def solve():
    T = int(input())
    MOD = 10**9 + 7

    dp = [[0] * (2001) for _ in range(2001)]

    for i in range(1, 2001):
        dp[i][1] = 1
    for j in range(1, 2001):
        dp[1][j] = 1

    for i in range(2, 2001):
        for j in range(2, 2001):
            dp[i][j] = (dp[i-1][j-1] + (i * (i+1) // 2) % MOD) % MOD

    ans = []
    for _ in range(T):
        N, M = map(int, input().split())
        ans.append(str(dp[N][M]))

    print('\n'.join(ans))

solve()
