python
def count_valid_sequences(N, A):
    MOD = 998244353

    # dp[i][j] will store the number of valid sequences of length i using numbers 1 to j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # There's one way to create an empty sequence

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1]  # Start with the number of ways without using j
            if A[j - 1] >= 1:
                dp[i][j] += dp[i - 1][j]  # Add the number of ways using j
                dp[i][j] %= MOD

    # The answer is the number of valid sequences of length N using numbers 1 to N
    result = dp[N][N]
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    result = count_valid_sequences(N, A)
    print(result)

