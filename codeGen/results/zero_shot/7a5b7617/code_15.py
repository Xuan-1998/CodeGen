import sys

def solve():
    T = int(sys.stdin.readline())
    MOD = 10**9 + 7

    dp = [[0] * (2001) for _ in range(2001)]
    dp[0][j] = 1 for j in range(2001)

    for i in range(1, N+1):
        for j in range(M+1):
            for s in range(j+1):
                dp[i][j] += (dp[i-1][s] * (j-s+1) % MOD)
            dp[i][j] %= MOD

    print(sum(dp[N][m] for m in range(2001)) % MOD)

if __name__ == "__main__":
    solve()
