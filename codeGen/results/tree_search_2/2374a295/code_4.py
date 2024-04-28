def goodSequences(n, k):
    MOD = 1000000007
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        for j in range(1, min(i, k) + 1):
            if i % j == 0:
                dp[i][j] = (dp[i - j][j - 1] + 1) % MOD
    
    return sum(dp[n][:k]) % MOD

# Read the input from stdin
n, k = map(int, input().split())

print(goodSequences(n, k))
