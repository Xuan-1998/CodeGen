python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Initialize the dp array
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case
    
    for i in range(N + 1):
        for j in range(M + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
                dp[i][j] %= MOD
            if j > 0:
                dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
            if i > 0 and j > 0:
                dp[i][j] -= dp[i - 1][j - 1]
                dp[i][j] %= MOD
    
    # The answer is the number of valid matrices of size NxM
    return dp[N][M]

import sys
input = sys.stdin.read
def main():
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

if __name__ == "__main__":
    main()

