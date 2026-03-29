def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(-1, n + 1):
        dp[i][0] = 1
    
    for j in range(1, n + 1):
        for i in range(j - 1, -1, -1):
            for k in range(i + 1, min(j, i) + 1):
                if all(int(digit) == int(dp[i][k]) % 10 for digit in str(i)[::-1]):
                    dp[i][j] = (dp[i][j] + dp[i - k][min(k, j)] * k) % MOD
    
    return ' '.join(str(dp[i][n]) for i in range(n))

n = int(input())
print(count_blocks(n))
