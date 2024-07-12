MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # dp[i][j] represents the number of ways to form a subtree with i vertices and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Iterate over the number of vertices
    for i in range(1, N + 1):
        # Iterate over the number of good vertices
        for j in range(1, i + 1):
            # Calculate dp[i][j] considering all possible splits
            for k in range(i):
                dp[i][j] += dp[k][j - 1] * dp[i - k - 1][0]
                dp[i][j] %= MOD
    
    # Sum up the number of good vertices for all possible subtree sizes
    result = 0
    for i in range(1, N + 1):
        result += dp[N][i]
        result %= MOD
    
    print(result)


