def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize dp table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 2  # A 1x1 matrix can either be 0 or 1
    
    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            # Transition: sum of ways to fill (i-1, j) and (i, j-1)
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    
    # The answer is the number of valid matrices of size NxM
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_valid_matrices(N, M)
    print(result)

