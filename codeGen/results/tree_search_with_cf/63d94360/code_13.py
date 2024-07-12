python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 1000000007
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # Initialize dp table
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        # Fill dp table
        for i in range(1, N + 1):
            for j in range(K + 1):
                dp[i][j] = sum(dp[i - 1][m] for m in range(K + 1) if m != j) % MOD
        
        # The result for this test case is dp[N][0]
        results.append(dp[N][0])
    
    for result in results:
        print(result)


