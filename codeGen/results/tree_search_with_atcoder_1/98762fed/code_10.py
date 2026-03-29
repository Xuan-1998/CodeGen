def count_valid_matrices(N, M):
    MOD = 998244353

    # Total number of 1s in all valid matrices
    total_ones = 0

    # We need to count the number of valid matrices and the number of ones in them
    # Initialize a DP table to store the number of valid matrices of size i x j
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1x1 matrix has 2 possibilities: [0] and [1]
    dp[1][1] = 2
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            
            # Number of valid matrices of size i x j
            dp[i][j] = (dp[i - 1][j] * 2 + dp[i][j - 1] * 2 - dp[i - 1][j - 1] * 2) % MOD
            
            # Count the number of ones in these matrices
            # Each valid matrix of size i x j can be built by adding a row or column to a valid matrix of smaller size
            total_ones = (total_ones + dp[i][j] * (i * j) // 2) % MOD

    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

