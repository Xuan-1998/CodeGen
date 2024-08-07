def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There's exactly one way to have a sequence of length 0
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i - 1][k] > 0 and A[j - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()

