MOD = 998244353

def count_valid_matrices(N, M):
    # Initialize the dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: a 0x0 matrix trivially satisfies the condition
    dp[0][0] = 1
    
    # Fill the dp array
    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 and j == 0:
                continue
            # Calculate number of ways to fill a matrix of size i x j
            dp[i][j] = 0
            if i > 0:
                dp[i][j] += dp[i-1][j] * (2 ** j)
                dp[i][j] %= MOD
            if j > 0:
                dp[i][j] += dp[i][j-1] * (2 ** i)
                dp[i][j] %= MOD
            if i > 0 and j > 0:
                dp[i][j] -= dp[i-1][j-1] * (2 ** (i + j - 1))
                dp[i][j] %= MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

