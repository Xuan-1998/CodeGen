def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    MOD = 10**9 + 7
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    def is_divisible(sub, k):
        for x in sub:
            if x % k != 0:
                return 0
        return 1
    
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(1, i+1):
            if a[j-1] % j == 0 and is_divisible(a[j:i], j):
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
    
    return sum(dp[n][i] for i in range(1, n+1)) % MOD

print(solve())
