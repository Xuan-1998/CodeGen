MOD = 998244353

def count_valid_sequences(N, A):
    # dp[i][j] will store the number of valid sequences of length i with j occurrences of each number
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: There is exactly 1 way to have a sequence of length 0 (the empty sequence)
    dp[0][0] = 1
    
    # Iterate over the length of the sequence
    for i in range(1, N + 1):
        # Iterate over the number of occurrences of the current number
        for j in range(N + 1):
            # If the number of occurrences is within the limit set by A[i-1]
            if j <= A[i - 1]:
                # Update the DP table
                for k in range(N - j + 1):
                    dp[i][k + j] = (dp[i][k + j] + dp[i - 1][k]) % MOD
    
    # The answer is the sum of all dp[N][j] for j from 0 to N
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

