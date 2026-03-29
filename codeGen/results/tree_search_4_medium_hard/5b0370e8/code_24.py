import sys

MOD = 10**9 + 7

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][j] = 1 for j in range(k+1)

        for i in range(1, n+1):
            for j in range(k+1):
                if j & (2**k - 1) <= i:
                    for x in range(j & (2**k - 1), j):
                        dp[i][j] += dp[i-1][x]
                    dp[i][j] %= MOD

        ans = sum(dp[n][j] for j in range(k+1))
        print(ans % MOD)

if __name__ == "__main__":
    solve()
