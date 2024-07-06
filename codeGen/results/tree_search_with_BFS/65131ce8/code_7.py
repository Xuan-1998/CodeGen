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
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(i):
            for k in range(1, N + 1):
                if i + k <= N:
                    dp[i + k][j + 1] = (dp[i + k][j + 1] + dp[i][j] * d[k - 1]) % MOD
    
    # Calculate the result
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


