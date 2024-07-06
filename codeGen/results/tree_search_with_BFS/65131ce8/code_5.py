MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: one node tree
    dp[1][1] = 1
    
    # Fill DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][1]) % MOD
    
    # Calculate the result
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


