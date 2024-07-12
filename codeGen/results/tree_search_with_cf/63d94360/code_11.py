MOD = 1000000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        for n in range(1, N + 1):
            for i in range(K + 1):
                dp[n][i] = sum(dp[n-1][j] for j in range(K + 1) if j != i) % MOD
        
        results.append(dp[N][0])
    
    for result in results:
        print(result)


