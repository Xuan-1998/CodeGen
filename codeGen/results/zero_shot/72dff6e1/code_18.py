python
def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(N + 1):
            for k in range(min(A[i - 1], j) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    
    # The answer is the number of ways to form a sequence of length N with sum N
    return dp[N][N]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    result = count_valid_sequences(N, A)
    print(result)

