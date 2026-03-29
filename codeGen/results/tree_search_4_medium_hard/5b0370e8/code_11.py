def solve():
    t = int(input())
    mod = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = {(i, j): 0 for i in range(n+1) for j in range(2**k)}

        dp[0][0] = 1
        for i in range(n):
            for j in range(2**k-1, -1, -1):
                if j & 1:  # LSB is 1
                    for x in range(j+1):
                        dp[i+1][x|j] += dp[i][x]
                    dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
                else:  # LSB is 0
                    if j < 2**k-1:
                        for x in range(j+1, 2**k):
                            dp[i+1][x|j] += dp[i][x]
        ans = sum(dp[n].values())
        print(ans % mod)

if __name__ == "__main__":
    solve()
