def count_good_sequences(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 1:
                dp[i][j] = 1
            elif j > 1:
                for d in range(2, i // (i % j) + 1):
                    if i % d == 0 and (i // d <= n or k - j < k):
                        dp[i][j] += dp[i // d][j - 1]
                        break
    
    return sum(dp[n]) % MOD

n, k = map(int, input().split())
print(count_good_sequences(n, k))
