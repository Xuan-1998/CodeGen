def count_good_sequences(n, k):
    MOD = 1000000007

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    def good_sequences(i, j):
        if i < 2 or j == 0:
            return 1
        if dp[i][j]:
            return dp[i][j]
        ans = good_sequences(i - 1, j - 1)
        ans += (i % k) * (ans % MOD)
        dp[i][j] = ans % MOD
        return ans

    return good_sequences(n, k)

# Read input from stdin
n, k = map(int, input().split())

print(count_good_sequences(n, k))
