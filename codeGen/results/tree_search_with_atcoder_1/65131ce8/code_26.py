python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill DP table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                for l in range(1, j + 1):
                    dp[i][j] = (dp[i][j] + dp[k][l] * dp[i - k][j - l]) % MOD
    
    # Calculate the result
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i]) % MOD
    
    print(result)


