python
MOD = 998244353

def count_valid_matrices(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 2
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            if i == 1:
                dp[i][j] = dp[i][j - 1] * 2 % MOD
            elif j == 1:
                dp[i][j] = dp[i - 1][j] * 2 % MOD
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    
    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

