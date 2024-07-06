def count_good_vertices(N, d):
    MOD = 998244353
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: 1 way to have 0 vertices and 0 good vertices
    
    for i in range(1, N + 1):
        for j in range(i + 1):
            if j > 0 and d[i - 1] > 0:
                dp[i][j] = (dp[i - 1][j - 1] * d[i - 1]) % MOD  # Make i-th vertex a good vertex
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD  # Not making i-th vertex a good vertex
    
    # Sum up all dp[N][j] where j is the number of good vertices
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    print(count_good_vertices(N, d))

