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
        for j in range(N + 1):
            if j >= d[i - 1]:
                dp[i][j] = dp[i - 1][j - d[i - 1]]
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
    
    # Calculate the number of good vertices
    good_vertices_sum = 0
    for i in range(1, N + 1):
        if dp[N][i] > 0:
            good_vertices_sum = (good_vertices_sum + dp[N][i]) % MOD
    
    print(good_vertices_sum)

if __name__ == "__main__":
    solve()

