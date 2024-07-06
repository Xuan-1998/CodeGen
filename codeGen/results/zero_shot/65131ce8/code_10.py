def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Process each vertex
    for i in range(1, N + 1):
        for j in range(i):
            for k in range(d[i - 1] + 1):
                if j + k <= N:
                    dp[i][j + k] = (dp[i][j + k] + dp[i - 1][j]) % MOD
    
    # Calculate the result
    result = sum(dp[N][i] * i for i in range(N + 1)) % MOD
    
    print(result)


