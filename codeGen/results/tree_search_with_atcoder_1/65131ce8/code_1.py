MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case
    dp[1][0] = 1
    
    # Fill dp table
    for i in range(2, N+1):
        for j in range(N):
            if j >= d[i-1]:
                for k in range(1, i):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Calculate the number of good vertices
    good_vertices_count = 0
    for i in range(1, N+1):
        for j in range(N):
            if dp[i][j] > 0 and j == d[i-1]:
                good_vertices_count = (good_vertices_count + dp[i][j]) % MOD
    
    print(good_vertices_count)


