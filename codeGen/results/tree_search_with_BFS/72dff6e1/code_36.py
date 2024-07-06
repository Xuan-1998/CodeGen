python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the DP table with zeros
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        if A[j - 1] >= 1:
            dp[1][j] = 1
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] >= i:
                for k in range(1, N + 1):
                    if A[k - 1] >= i - 1:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Calculate the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    print(count_valid_sequences(N, A))

