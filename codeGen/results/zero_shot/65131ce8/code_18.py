MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))

    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Fill DP table
    for i in range(1, N + 1):
        for j in range(N):
            for k in range(1, N - j + 1):
                if j + k <= N:
                    dp[i][j + k] = (dp[i][j + k] + dp[i - 1][j]) % MOD
    
    # Calculate number of good vertices
    good_vertices = 0
    for i in range(1, N + 1):
        good_vertices = (good_vertices + dp[i][N - 1]) % MOD
    
    print(good_vertices)


