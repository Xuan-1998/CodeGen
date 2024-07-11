def solve():
    MOD = 998244353
    N = int(input().strip())
    D = list(map(int, input().strip().split()))

    if D[0] != 1 or D.count(0) != 1:
        return 0

    dp = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
    dp[1][1][1] = 1
    cnt = [0] * (N + 1)
    for d in D:
        cnt[d] += 1

    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(j + 1):
                dp[i][j][0] += dp[i - 1][k][0] * cnt[j - 1] % MOD
                dp[i][j][0] += dp[i - 1][k][1] * max(0, cnt[j - 1] - (j == k)) % MOD
                dp[i][j][1] += dp[i - 1][k][0] * cnt[j - 1] % MOD
                dp[i][j][1] += dp[i - 1][k][1] * max(0, cnt[j] - (j == k)) % MOD

    res = sum(dp[N][j][1] for j in range(1, N + 1)) % MOD
    return res


print(solve())

