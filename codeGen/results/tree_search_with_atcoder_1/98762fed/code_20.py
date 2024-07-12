python
MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize the DP table with all zeros
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            # Extend from smaller matrices
            if i > 1:
                # Adding a new row to (i-1)xj matrix
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j > 1:
                # Adding a new column to ix(j-1) matrix
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
    
    # The answer is the number of valid matrices of size NxM
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

