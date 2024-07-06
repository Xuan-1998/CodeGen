MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will store the number of ways to form a sequence of length i
    # with exactly j occurrences of each number from 1 to N
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to form an empty sequence

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(A[j-1] + 1):
                if i >= k:
                    dp[i][j] = (dp[i][j] + dp[i - k][j - 1]) % MOD

    # The result is the number of ways to form a sequence of length N
    result = dp[N][N]
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

