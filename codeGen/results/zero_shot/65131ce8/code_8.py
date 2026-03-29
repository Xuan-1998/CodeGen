def solve():
    MOD = 998244353
    N = int(input())
    D = list(map(int, input().split()))
    if D[0] != 1 or D.count(0) != 1:
        print(0)
        return
    D.sort()
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j - 1] * D[i - 1] % MOD
            if j >= 1:
                dp[i][j] += dp[i - 1][j] * (i - D[i - 1]) % MOD
    print(sum(dp[N - 1]) % MOD)

solve()

