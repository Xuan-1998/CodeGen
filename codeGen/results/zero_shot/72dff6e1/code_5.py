MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will store the number of ways to form a valid sequence of length i
    # where j is the current element being considered
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # There's one way to form a sequence of length 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(A[j - 1] + 1):
                if i >= k:
                    dp[i][j] = (dp[i][j] + dp[i - k][j - 1]) % MOD
    
    # Sum up all valid sequences of length N
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    result = count_valid_sequences(N, A)
    print(result)

