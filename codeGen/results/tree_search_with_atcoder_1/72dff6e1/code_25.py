python
MOD = 998244353

def count_valid_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to have an empty sequence

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i-1][k] > 0:
                    # Check if adding j to the sequence ending with k is valid
                    if sum(dp[i-1][k] for k in range(1, N + 1)) <= A[j-1]:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    # Sum up all sequences of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

