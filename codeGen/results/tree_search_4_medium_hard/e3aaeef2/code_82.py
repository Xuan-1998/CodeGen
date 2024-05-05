def solve():
    t = int(input())
    MOD = 10**9 + 7
    
    dp = [[0] * (2*10**5+1) for _ in range(10**9+1)]
    
    for i in range(10**9+1):
        dp[i][0] = len(str(i))
        
    for m in range(2*10**5+1):
        for i in range(10**9+1):
            if i == 0:
                continue
            carry_i = 0
            for d in str(i):
                carry_i = (carry_i * 10 + int(d) + 1) % MOD
            dp[i][m] = min(len(str(i)) + 1, dp[carry_i][m-1])
            
    for _ in range(t):
        n, m = map(int, input().split())
        print(dp[n][m])

solve()
