python
MOD = 998244353

def count_valid_sequences(N, A):
    # Create a DP array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize base case
    dp[0][0] = 1
    
    # Update DP table
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
            if j > A[i - 1]:
                dp[i][j] -= dp[i - 1][j - A[i - 1] - 1]
                dp[i][j] += MOD
                dp[i][j] %= MOD
    
    # Result is the sum of dp[N][j] for all valid j
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

