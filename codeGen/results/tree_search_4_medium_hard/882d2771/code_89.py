def solve():
    t, l, r = map(int, input().split())
    MOD = 10**9 + 7

    # Initialize memoization array
    dp = [[0] * (l+1) for _ in range(r+1)]

    for i in range(l):
        dp[i][i] = 1

    for r in range(2, r+1):
        for l in range(max(0, r-5), min(r, l)+1):
            if l == 1:
                dp[l][r] = (r - 1) % MOD
            else:
                dp[l][r] = min((dp[l-1][min(r, l-1)] + (r - (l-1))) % MOD, 
                                (dp[min(r, l-2)][l-1]) % MOD) + 1

    res = 0
    for i in range(t):
        res += dp[0][r-i]
    print(res % MOD)

if __name__ == "__main__":
    solve()
