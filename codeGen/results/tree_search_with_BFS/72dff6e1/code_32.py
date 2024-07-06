python
MOD = 998244353

def count_valid_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case
    dp[0][0] = 1
    
    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, j + 1):
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD
    
    # Calculate the final answer
    result = 0
    for j in range(1, N + 1):
        result += dp[N][j]
        result %= MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

