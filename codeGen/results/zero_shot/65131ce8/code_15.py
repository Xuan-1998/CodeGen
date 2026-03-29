def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Initialize the DP array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # DP to count the number of ways to distribute the out-degrees
    for i in range(1, N + 1):
        for j in range(N + 1):
            if j >= d[i - 1]:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - d[i - 1]]) % MOD
            else:
                dp[i][j] = dp[i - 1][j] % MOD
    
    # Calculate the sum of good vertices
    good_vertices_sum = 0
    for i in range(1, N + 1):
        if d[i - 1] == 0:
            good_vertices_sum = (good_vertices_sum + dp[N][N - 1]) % MOD
    
    print(good_vertices_sum)


