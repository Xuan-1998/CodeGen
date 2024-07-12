MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: dp[v][0] = 1
    for v in range(1, N + 1):
        dp[v][0] = 1
    
    # Calculate dp states
    for v in range(N, 0, -1):
        out_degree = d[v - 1]
        for k in range(1, N + 1):
            dp[v][k] = dp[v][k - 1]
            for child in range(v + 1, v + out_degree + 1):
                if child <= N:
                    dp[v][k] += dp[child][k - 1]
                    dp[v][k] %= MOD
    
    # Calculate the sum of good vertices
    result = 0
    for v in range(1, N + 1):
        result += dp[v][v]
        result %= MOD
    
    print(result)


