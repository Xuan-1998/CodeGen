python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 1000000007
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # dp[i][j] will store the number of ways to reach player j after i passes
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Initialize: The ball can start with any player
        for j in range(K + 1):
            dp[0][j] = 1
        
        # Fill the dp table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = 0
                for m in range(K + 1):
                    if m != j:
                        dp[i][j] = (dp[i][j] + dp[i - 1][m]) % MOD
        
        # The result is the number of ways to reach player P after N passes
        results.append(dp[N][0])
    
    for result in results:
        print(result)


