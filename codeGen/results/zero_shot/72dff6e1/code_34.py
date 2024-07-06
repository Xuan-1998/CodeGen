python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Iterate over the positions in the sequence
    for i in range(1, N + 1):
        # Iterate over the possible counts of each number
        for j in range(N + 1):
            # If we don't use the number i at all
            dp[i][j] = dp[i-1][j]
            # If we use the number i at least once
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1] * A[i-1]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

