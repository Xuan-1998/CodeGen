MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to form an empty sequence
    
    for i in range(1, N + 1):
        for j in range(N + 1):
            dp[i][j] = dp[i-1][j]  # Carry forward the previous count
            if j > 0:
                dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    result = 1
    for i in range(1, N + 1):
        result = result * dp[i][A[i-1]] % MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

