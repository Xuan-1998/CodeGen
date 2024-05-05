def main():
    n = int(input())
    MOD = 998244353
    
    dp = [[0] * (1 << n) for _ in range(n + 1)]
    
    # base case: no tower used
    for j in range(1 << n):
        if all((j >> i) & 1 for i in range(n)):
            dp[0][j] = 2 ** ((n + 1))
    
    for i in range(1, n + 1):
        for j in range(1 << n):
            # consider two possibilities: use or don't use the current tower
            if (j >> (i - 1)) & 1:
                dp[i][j] = (dp[i - 1][j ^ (1 << (i - 1))] + dp[i - 1][0]) % MOD
            else:
                dp[i][j] = (dp[i - 1][j] * 2) % MOD
    
    # the final answer is the difference between two cases: use and don't use any tower
    print((dp[n][0] - dp[n - 1][0]) % MOD)

if __name__ == "__main__":
    main()
