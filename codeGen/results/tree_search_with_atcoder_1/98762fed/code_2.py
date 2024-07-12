python
MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize the DP table
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: there are 2 valid 1x1 matrices (either 0 or 1)
    dp[1][1] = 2
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) % MOD
    
    # The answer is the number of valid NxM matrices
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

