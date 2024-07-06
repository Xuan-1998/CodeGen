MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    # dp[i][j] will store the number of valid i x j matrices
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: There's only one 1x1 matrix with a single element (either 0 or 1)
    dp[1][1] = 2
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + MOD) % MOD
    
    # The result for N x M matrix
    result = dp[N][M]
    print(result)


