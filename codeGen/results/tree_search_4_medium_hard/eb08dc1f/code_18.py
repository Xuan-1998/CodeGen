def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: Count blocks ending at each digit position with length 1
    for i in range(n + 1):
        dp[i][1] = 10 ** i % MOD
    
    # Fill up the dynamic programming table
    for i in range(2, n + 1):
        for k in range(1, min(i, n) + 1):
            for j in range(max(0, i - k), i):
                dp[i][k] += (dp[j][k - 1] * (10 ** (i - j) % MOD)) % MOD
    
    # Calculate the total count of blocks
    ans = sum(dp[n][k] for k in range(1, n + 1))
    
    return ans

n = int(input())
print(count_blocks(n))
