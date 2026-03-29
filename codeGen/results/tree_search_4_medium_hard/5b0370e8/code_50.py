def solve():
    t = int(input())
    MOD = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (2**k) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(k):
                for s in range(2**k):
                    if not ((s >> (k-j-1)) & 1):  # last bit is 0
                        dp[i][j] += sum(dp[i-1][t] for t in range(2**k))

        res = sum(dp[n][j] for j in range(k))
        print(res % MOD)

if __name__ == "__main__":
    solve()
