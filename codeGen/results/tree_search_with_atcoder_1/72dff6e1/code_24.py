python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Fill the DP table for lengths 2 to N
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = 0
            for k in range(1, N + 1):
                if dp[i-1][k] > 0 and dp[i-1][k] <= A[j-1]:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    print(count_valid_sequences(N, A))

