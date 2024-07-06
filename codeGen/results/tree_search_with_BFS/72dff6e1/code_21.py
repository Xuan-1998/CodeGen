python
MOD = 998244353

def count_valid_sequences(N, A):
    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    # Count occurrences of each number in the sequence
    counts = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if counts[i-1][k] < A[k-1]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
                    counts[i][j] = counts[i-1][k] + 1

    # Sum up the valid sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

