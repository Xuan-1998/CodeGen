def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = (dp[i-1] * (i - m[i-1] + 1)) % MOD
    
    print(dp[-1])
