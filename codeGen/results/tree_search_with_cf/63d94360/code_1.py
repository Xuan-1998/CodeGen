MOD = 1000000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx + 1])
        idx += 2
        
        # Initialize DP table
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        # Fill DP table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i-1][m] for m in range(K + 1) if m != j) % MOD
        
        # The result is the number of ways to make exactly N passes ending with player 0
        results.append(dp[N][0])
    
    for result in results:
        print(result)


