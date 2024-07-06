python
def count_valid_sequences(N, A):
    MOD = 998244353

    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There's one way to have a sequence of length 0
    dp[0][0] = 1

    # Iterate over each length of sequence
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[j - 1] >= i:
                dp[i][j] = dp[i - 1][j - 1] % MOD
            for k in range(1, N + 1):
                if A[k - 1] >= i and A[j - 1] >= dp[i][k]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

    # Sum up all valid sequences of length N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

