python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # base case
    
    for i in range(1, N + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1] * d[i - 1] % MOD  # if i-th vertex is a good vertex
            dp[i][j] += dp[i - 1][j] * (i - 1 - (j - 1)) % MOD  # if i-th vertex is not a good vertex
            dp[i][j] %= MOD
    
    result = sum(dp[N]) % MOD
    print(result)


