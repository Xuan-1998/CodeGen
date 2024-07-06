python
MOD = 998244353

def count_valid_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Initialize dp for sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Count occurrences of each number in sequences ending with each number
    count = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            count[i][j] = count[i - 1][j]
        
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if count[i - 1][k] < A[k] and count[i][j] < A[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
                    count[i][j] += 1
    
    # Calculate the final answer
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    print(count_valid_sequences(N, A))

