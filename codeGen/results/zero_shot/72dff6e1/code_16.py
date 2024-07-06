python
MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] means the number of ways to form a sequence of length i with exactly j different elements
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            for k in range(1, N + 1):
                if A[k - 1] >= j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
                if A[k - 1] >= j - 1:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
    
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

