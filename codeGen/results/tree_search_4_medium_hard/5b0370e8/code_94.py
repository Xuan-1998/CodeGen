def solve():
    t = int(input())
    mod = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n+1)]

        for i in range(k-1, -1, -1):
            if i == k-1:
                dp[i][0] = 2**k
            else:
                for j in range(1 << k):
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod

        ans = sum(dp[n][i] for i in range(1 << k))
        print(ans)

if __name__ == "__main__":
    solve()
