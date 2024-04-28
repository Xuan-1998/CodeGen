def solve():
    n, k = map(int, input().split())
    MOD = 10**9 + 7

    def good_sequences(k, n):
        if k == 0:
            return 1
        dp = {0: 1}
        for i in range(1, n+1):
            if i not in dp:
                continue
            for j in range(i-1, 0, -1):
                if j * i > n:
                    break
                if j not in dp:
                    dp[j*i] = good_sequences(k-1, j)
                dp[j*i] += dp[i]
        return dp[n] % MOD

    print(good_sequences(k, n))

solve()
