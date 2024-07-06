python
MOD = 998244353

def count_sequences(N, A):
    # dp[i][j] will store the number of valid sequences of length i ending with number j
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequence of length 0
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        # Iterate over the possible ending number
        for j in range(1, N + 1):
            # Sum up the valid sequences from the previous length
            for k in range(1, N + 1):
                if k != j and dp[i-1][k] > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Calculate the final answer
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
    
    print(count_sequences(N, A))

