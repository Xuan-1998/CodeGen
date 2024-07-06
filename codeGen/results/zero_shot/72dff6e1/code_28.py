python
MOD = 998244353

def count_valid_sequences(N, A):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        prefix_sum = [0] * (N + 1)
        for j in range(1, N + 1):
            prefix_sum[j] = (prefix_sum[j - 1] + dp[i - 1][j]) % MOD
        
        for j in range(1, N + 1):
            if i <= A[j - 1]:
                dp[i][j] = prefix_sum[j]
    
    result = sum(dp[N]) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    print(count_valid_sequences(N, A))

