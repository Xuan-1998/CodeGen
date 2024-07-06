python
def count_valid_sequences(N, A):
    MOD = 998244353
    
    # Initialize DP table with zeros
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    # Base case: one way to have an empty sequence
    dp[0][0] = 1
    
    # Fill DP table
    for i in range(1, N+1):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j]  # Not using the number i
            if j > 0:
                dp[i][j] += dp[i][j-1]  # Using the number i
                dp[i][j] %= MOD
    
    # Calculate the result
    result = 0
    for i in range(1, N+1):
        result += dp[N][A[i-1]]
        result %= MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

