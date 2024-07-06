python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Fill DP table
    for i in range(1, N + 1):
        for j in range(N + 1):
            if j >= d[i - 1]:
                dp[i][j] = dp[i - 1][j - d[i - 1]]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD
    
    # Calculate the result
    result = 0
    for i in range(1, N + 1):
        if d[i - 1] == 0:
            result += dp[N][i]
            result %= MOD
    
    print(result)


