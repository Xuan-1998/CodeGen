python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] = dp[i - 1][j - 1] * (N - i + 1) % MOD
            if i > 1:
                dp[i][j] = (dp[i][j] + dp[i - 1][j] * (i - 1)) % MOD
    
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


