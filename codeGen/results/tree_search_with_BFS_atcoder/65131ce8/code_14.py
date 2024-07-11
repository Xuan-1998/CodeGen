MOD = 998244353

def solve():
    N = int(input())
    d = list(map(int, input().split()))
    d = [0] + d

    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[1][1] = 1

    for i in range(2, N+1):
        dp[i][1] = dp[i-1][d[i-1]]
        for j in range(2, i+1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]*d[i-1]) % MOD

    ans = 0
    for j in range(1, N+1):
        ans = (ans + dp[N][j]) % MOD
    print(ans)

solve()

