python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][0] = 1  # base case: single vertex with out-degree 0
    
    # Fill dp array
    for i in range(2, N + 1):
        for j in range(N):
            if d[j] > 0:
                for k in range(1, i):
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][0]) % MOD
    
    # Calculate the number of good vertices
    good_vertices_count = 0
    for i in range(1, N + 1):
        if d[i - 1] == 0:
            good_vertices_count = (good_vertices_count + dp[N][i - 1]) % MOD
    
    print(good_vertices_count)


