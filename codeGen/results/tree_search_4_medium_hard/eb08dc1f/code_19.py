def solve(n):
    MOD = 998244353
    dp = [0] * (n + 1)
    
    # Base case: Counting total number of blocks
    for i in range(10):
        dp[0] += 1
    
    for k in range(1, n + 1):
        for j in range(1, k + 1):
            dp[k] = (dp[k] + sum((int(str(i) * '0' * (k - j)) % MOD for i in range(10))) % MOD)
    
    # Calculate the result as the sum of the counts for all lengths
    return ' '.join(map(str, [dp[i] % MOD for i in range(n + 1)]))

n = int(input())
print(solve(n))
