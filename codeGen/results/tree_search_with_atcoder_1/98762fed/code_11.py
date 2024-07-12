python
MOD = 998244353

def count_valid_matrices(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case
    dp[1][1] = 2  # A 1x1 matrix can be either [0] or [1]
    
    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    
    # Sum all dp[i][j] values
    result = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            result = (result + dp[i][j]) % MOD
            
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    print(count_valid_matrices(N, M))

