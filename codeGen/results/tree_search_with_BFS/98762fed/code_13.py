python
def count_ones_in_valid_matrices(N, M):
    MOD = 998244353

    # Initialize a 2D dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Fill the dp array
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + MOD) % MOD

    # Calculate the total number of 1s in all valid matrices
    total_ones = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            total_ones = (total_ones + dp[i][j] * i * j) % MOD

    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    result = count_ones_in_valid_matrices(N, M)
    print(result)

